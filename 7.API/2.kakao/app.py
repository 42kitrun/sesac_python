from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for,session
import requests
import os
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

KAKAO_REST_API_KEY = os.getenv("KAKAO_REST_API_KEY")
KAKAO_REDIRECT_URI = os.getenv("KAKAO_REDIRECT_URI")

KAKAO_CLIENT_SECRET = os.getenv("KAKAO_CLIENT_SECRET")

@app.route('/')
def index():
    user = session.get('user') # flask에서 session ID 자동 발급
    return render_template('index.html', user=user)

@app.route('/auth/kakao')
def login_kakao():
    # 선택: 사용자에게 추가 동의를 요청하는 경우, scope 값으로 동의항목 ID를 전달
    # 친구 목록, 메시지 전송 등 접근권한 요청 가능
    # (예: /authorize?scope=friends,talk_message)
    scope_param = ""
    if request.args.get("scope"):
        scope_param = "&scope=" + request.args.get("scope")

    kakao_auth_url = (
        # 카카오 로그인 주소 엔드포인트 찾아오기, 또한 필요한 입력값들 확인하기
        f"https://kauth.kakao.com/oauth/authorize?"
        f"response_type=code&client_id={KAKAO_REST_API_KEY}"
        f"&redirect_uri={KAKAO_REDIRECT_URI}{scope_param}"
    )
    return redirect(kakao_auth_url)

@app.route('/auth/kakao/callback')
def callback():
    code = request.args.get('code')  # 서버가 인증 성공의 댓가로 준 값
    state = request.args.get('state')  # 내 사이트에서 갔다 온건지 확인용, 내가 보낸 글자 잘 왔는지 확인
    print(f"code: {code}, state: {state}")
    
    # 카카오에게 코드 검증후 토큰을 발급받을 엔드포인트 및 입력값 확인하기
    # 인가 코드 발급 요청에 필요한 파라미터 구성
    data = {
        'grant_type': 'authorization_code',  # 인증 방식 고정값
        'client_id': KAKAO_REST_API_KEY,              # 내 앱의 REST API 키
        'redirect_uri': KAKAO_REDIRECT_URI,        # 등록된 리다이렉트 URI
        'client_secret': KAKAO_CLIENT_SECRET,      # 선택: 클라이언트 시크릿(Client Secret) 사용 시 추가
        'code': code     # 전달받은 인가 코드
    }

    # 카카오 인증 서버에 액세스 토큰 요청
    resp = requests.post( "https://kauth.kakao.com/oauth/token", data=data)

    # 발급받은 액세스 토큰을 세션에 저장 (로그인 상태 유지 목적)
    session['access_token'] = resp.json()['access_token']
    
    return redirect(url_for('profile'))

# 액세스 토큰을 사용해 로그인한 사용자의 정보 조회 요청
@app.route("/profile")
def profile():
    headers = {
        'Authorization': 'Bearer ' + session.get('access_token', '')  # 세션에 저장된 액세스 토큰 전달
    }

    req = requests.get( "https://kapi.kakao.com/v2/user/me", headers=headers)  # 사용자 정보 조회 API 요청 전송
    print(req.text)  # 조회한 사용자 정보를 클라이언트에 반환
    '''{
        "id":4357384534,
        "connected_at":"2025-08-03T12:58:46Z",
        "properties":{
            "nickname":"매미",
            "profile_image":"http://k.kakaocdn.net/dn/cSOBXq/btqXLfl3h4P/XekxieXDEWEXVGYHowj83D/img_640x640.jpg",
            "thumbnail_image":"http://k.kakaocdn.net/dn/cSOBXq/btqXLfl3h4P/XekxieXDEWEXVGYHowj83D/img_110x110.jpg"
        },
        "kakao_account":{
            "profile_nickname_needs_agreement":false,
            "profile_image_needs_agreement":false,
            "profile":{
                "nickname":"매미",
                "thumbnail_image_url":"http://k.kakaocdn.net/dn/cSOBXq/btqXLfl3h4P/XekxieXDEWEXVGYHowj83D/img_110x110.jpg",
                "profile_image_url":"http://k.kakaocdn.net/dn/cSOBXq/btqXLfl3h4P/XekxieXDEWEXVGYHowj83D/img_640x640.jpg",
                "is_default_image":false,
                "is_default_nickname":false
            }
        }
    }'''

    # 응답 JSON 형태로 변환
    user_info = req.json()
    user = user_info.get('properties')
    print(user)
    # 위에 내용 다 끝나면?? 사용자 정보 저장하고, 수정하고 등등 기능 추가

    return render_template("index.html", user=user)

# 로그아웃 추가하기
# 로그아웃 요청: 세션을 종료하고 사용자 로그아웃 처리
@app.route("/logout")
def logout():
    headers = {
        'Authorization': 'Bearer ' + session.get('access_token', '')  # 세션에 저장된 액세스 토큰 전달
    }
    resp = requests.post("https://kapi.kakao.com/v1/user/logout", headers=headers)  # 카카오 API에 로그아웃 요청 전송
    session.pop('access_token', None)  # 세션 삭제 (로그아웃 처리)
    print(resp.text)  # 응답 결과 클라이언트에 반환

    return redirect(url_for('index'))

# 연결 해제 요청: 사용자와 앱의 연결을 해제하고 세션 종료
@app.route("/unlink")
def unlink():
    headers = {
        'Authorization': 'Bearer ' + session.get('access_token', '')  # 세션에 저장된 액세스 토큰 전달
    }
    resp = requests.post("https://kapi.kakao.com/v1/user/unlink", headers=headers)  # 카카오 API에 연결 해제 요청 전송
    session.pop('access_token', None)  # 세션 삭제 (연결 해제 처리)
    print(resp.text)  # 응답 결과 클라이언트에 반환

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
    