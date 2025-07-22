from flask import Blueprint,send_from_directory,jsonify,request
import be.item.model as model

item_bp = Blueprint('item', __name__
                                    # , root_path=os.path.abspath(os.path.dirname(__file__ + "/../.."))
                                    , root_path='/Users/seSAC/src/sesac_python/5.Project/5.crm'
                                    , static_folder = 'fe/static/item'   # 실제 파일(하드디스크, 코드상 폴더) 위치
                                    , static_url_path = '/fe/static/item' # 브라우저에서 접근할 때 사용할 URL 주소(URL(주소창)은 웹 서버의 루트(/)를 기준)
)

@item_bp.route("/", methods=["GET","POST"])
def item():
    return send_from_directory(item_bp.static_folder + '/list', 'index.html')

@item_bp.route('/api/list',methods=["POST"])
def api_item_list():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print(query)

    items = model.item_list(query)
    print('api 전송 직전',items['data'][0], items['paging'])
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(items)