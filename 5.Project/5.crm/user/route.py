import sys
sys.path.append('5.Project/5.crm')

from flask import Blueprint,send_from_directory,jsonify
import user.model as db

user_bp = Blueprint('user', __name__, static_folder = 'static/user'   # 실제 파일(하드디스크, 코드상 폴더) 위치
                                    , static_url_path = '/static/user' # 브라우저에서 접근할 때 사용할 URL 주소(URL(주소창)은 웹 서버의 루트(/)를 기준)
)

@user_bp.route("/")
def user_list():
    return send_from_directory(user_bp.static_folder + '/list', 'index.html')

@user_bp.route('/api/list')
def api_user_list():
    users = db.get_users()
    print(users)

    return jsonify(users)