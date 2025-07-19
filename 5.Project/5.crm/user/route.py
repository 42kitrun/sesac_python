from flask import Blueprint,send_from_directory,jsonify,request,redirect,url_for
import user.model as model

import os
user_bp = Blueprint('user', __name__
                                    # , root_path=os.path.abspath(os.path.dirname(__file__ + "/../.."))
                                    , root_path='/Users/seSAC/src/sesac_python/5.Project/5.crm'
                                    , static_folder = 'static/user'   # 실제 파일(하드디스크, 코드상 폴더) 위치
                                    , static_url_path = '/static/user' # 브라우저에서 접근할 때 사용할 URL 주소(URL(주소창)은 웹 서버의 루트(/)를 기준)
)

@user_bp.route("/", methods=["GET","POST"])
def user():
    return send_from_directory(user_bp.static_folder + '/list', 'index.html')

@user_bp.route("/search", methods=["POST"])
def search_query():
    name = request.form.get('name')
    gender = request.form.get('gender')
    # POST 후에 결과를 쿼리 파라미터로 실어 보냄
    return redirect(url_for('user.user', name=name, gender=gender))

@user_bp.route('/api/list',methods=["POST"])
def api_user_list():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print(query)

    users = model.user_list(query)
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(users)