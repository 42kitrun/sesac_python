from flask import Blueprint,send_from_directory,jsonify,request
import be.user.model as model

user_bp = Blueprint('user', __name__
                                    # , root_path=os.path.abspath(os.path.dirname(__file__ + "/../.."))
                                    , root_path='/Users/seSAC/src/sesac_python/5.Project/5.crm'
                                    , static_folder = 'fe/static/user'   # 실제 파일(하드디스크, 코드상 폴더) 위치
                                    , static_url_path = '/fe/static/user' # 브라우저에서 접근할 때 사용할 URL 주소(URL(주소창)은 웹 서버의 루트(/)를 기준)
)

## user
@user_bp.route("/", methods=["GET","POST"])
def user():
    return send_from_directory(user_bp.static_folder + '/list', 'index.html')

## user/0a497257-2b1a-4836-940f-7b95db952e61/?listCount=10&page=3
@user_bp.route("/<uuid:user_id>", methods=["GET", "POST"])
def user_detail(user_id):
    return send_from_directory(user_bp.static_folder + '/detail', 'index.html')

# ------------------------------------------------------------------------------------

@user_bp.route('/api/list',methods=["POST"])
def api_user_list():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print(query)

    users = model.user_list(query)
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(users)

@user_bp.route('/api/<uuid:user_id>/favorite-stores/top5',methods=["GET"])
def api_user_detail_top5(user_id):
    query = {'user_id':user_id}

    top_5 = model.user_detail_top5(query)
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(top_5)