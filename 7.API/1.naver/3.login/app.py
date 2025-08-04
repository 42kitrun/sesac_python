from flask import Flask, render_template, redirect, request, url_for, session
from dotenv import load_dotenv
import os,json
import requests
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

# TODO: sqlite 와 연동해서.. 사용자 정보 저장하기..

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET") # 세션 암호화를 위한 키 (내가 관리하고, 내가 암호화 하고 내가 복호화 하고, 즉 외부에 노출되면 안됨)

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_REDIRECT_URI = os.getenv("NAVER_REDIRECT_URI")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///naver.db' # instance/naver.db flask에서 자동 폴더 생성함
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
app.config['SESSION_COOKIE_HTTPONLY'] = True     # XSS 공격 방지 : JavaScript로 쿠키 접근 차단
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'    # CSRF 공격 방지 : 다른 사이트에서 쿠키 전송 제한

# 최종적으로받아온사용자정보
# profile: {
#   'resultcode': '00',
#   'message': 'success',
#   'response': {
#     'id': 'qjwekrljsdlfjwei23SDF239xdfQSDf',
#     'nickname': 'tor',
#     'age': '50-59',
#     'gender': 'F'
#   }
# }    
# 모델 정의 (SQLAlchemy 초기화 후에 해야 함)
class User(db.Model):
    user_id = db.Column(db.String(255), primary_key=True)
    nickname = db.Column(db.String(255), nullable=False)
    age = db.Column(db.String(15))
    gender = db.Column(db.String(1))

# Flask-Session 초기화 (모델 정의 후에 해야 함)
Session(app)

@app.route('/')
def index():
    user = session.get('user') #flask가 session ID 발급
    return render_template('index.html', user=user)

@app.route('/login/naver/')
def login_naver():
    # 실제 네이버 로그인 인증 할 주소
    auth_url = (
        f"https://nid.naver.com/oauth2.0/authorize?"
        f"response_type=code&client_id={NAVER_CLIENT_ID}"
        f"&redirect_uri={NAVER_REDIRECT_URI}&state=xyz"
    )
    return redirect(auth_url)

@app.route('/naver/callback') # 네이버 인증 끝난 이후에 돌아올 곳
def naver_callback():

    code = request.args.get('code')  # 서버(네이버)가 인증 성공의 댓가로 준 값 : 이걸로 네이버와 확인
    state = request.args.get('state')  # 내 사이트에서 갔다 온건지 확인용, 내가 보낸 글자 잘 왔는지 확인
    print(f"code: {code}, state: {state}")
    # 내가 네이버와 앞으로 대화하기 위한 인증 토큰 요청 (code를 검증한 이후 맞으면 서버는 토큰을 줌)
    token_url = (
        f"https://nid.naver.com/oauth2.0/token?"
        f"grant_type=authorization_code&client_id={NAVER_CLIENT_ID}"
        f"&client_secret={NAVER_CLIENT_SECRET}&code={code}&state={state}"
    )
    
    # (code를 검증한 이후 서버가 준 토큰)
    token_response = requests.get(token_url).json()
    print(token_response)
    access_token = token_response.get('access_token')
    
    # 이제 사용자가 제대로 인증하고 온것 확인했으니, 나도 서버(naver)에게 해당 사용자의 정보를 달라고 하자.
    headers = {"Authorization": f"Bearer {access_token}"}
    profile = requests.get('https://openapi.naver.com/v1/nid/me', headers=headers).json()
    
    print('최종적으로 받아온 사용자 정보: ', profile)

    # TODO: 우리의 DB(sqlite3) 에 이 사용자가 있는지 확인하고, 있으면 그 정보 가져와서 세션에 저장
    #       해당 사용자가 없으면? 새롭게 DB에 삽입.
    #       이걸 더 확장하고 싶으면?? 사용자가 없으면, 그때 회원가입 페이지로 보내서.. "주소", "전화번호" 등 추가정보를 입력받게해서 DB에 저장한다.
    
    profile_response = profile['response']
    naver_user_id = profile_response['id']  # 네이버에서 제공하는 고유 ID

    # 데이터베이스에 영구 저장할 사용자 정보
    # DB에서 사용자 확인/생성 
    user = User.query.get(naver_user_id)
    if not user:
        # 새 사용자 생성
        user = User(
            user_id=naver_user_id,
            nickname=profile_response['nickname'],  # 'nickname' 키가 없으면 KeyError 발생 → 프로그램 중단
            age=profile_response.get('age'),        # 'age' 키가 없으면 None 반환 → 프로그램 계속 실행
            gender=profile_response.get('gender')   # None이면 NULL로 저장
        )
        db.session.add(user)
        db.session.commit()
        print(f"새 사용자 생성: {naver_user_id}")
    else:
        print(f"기존 사용자 로그인: {naver_user_id}")
    
    # 현재 로그인 세션에서 임시 사용할 정보
    # 사용자 정보를 내 세션에 저장하기
    session['user'] = {
        'user_id': user.user_id,
        'nickname': user.nickname,
        'age': user.age,
        'gender': user.gender
    }

    user = User.query.get(naver_user_id)

    return redirect(url_for('index', user=user))     

@app.route('/profile', methods=['GET','POST'])
def profile():
    if not session.get('user'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        nickname = request.form.get('nickname')
        age = request.form.get('age')
        gender = request.form.get('gender')
        
        

    user = session['user']
    print(user)

    # 연령대 리스트
    ages = ['10-19',
            '20-29',
            '30-39',
            '40-49',
            '50-59',
            '60-69',
            '70-79',
            '80-89'
    ]
    return render_template('profile.html',user=user, ages=ages)

@app.route('/logout')
def logout():
    if not session.get('user'):
        return redirect(url_for('index'))

    session.clear() # 이 사용자의 세션 모두 삭제
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        print("여기 들어왔나?")
        db.create_all()
        
    app.run(debug=True)