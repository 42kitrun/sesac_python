from flask import Blueprint,send_from_directory,jsonify,request
import be.order_item.model as model

order_item_bp = Blueprint('orderitem', __name__
                                    # , root_path=os.path.abspath(os.path.dirname(__file__ + "/../.."))
                                    , root_path='/Users/seSAC/src/sesac_python/5.Project/5.crm'
                                    , static_folder = 'fe/static/order_item'   # 실제 파일(하드디스크, 코드상 폴더) 위치
                                    , static_url_path = '/fe/static/order_item' # 브라우저에서 접근할 때 사용할 URL 주소(URL(주소창)은 웹 서버의 루트(/)를 기준)
)

@order_item_bp.route("/", methods=["GET","POST"])
def order_item():
    return send_from_directory(order_item_bp.static_folder + '/list', 'index.html')

## orderitem/0a497257-2b1a-4836-940f-7b95db952e61/?listCount=10&page=3
@order_item_bp.route("/<uuid:order_item_id>", methods=["GET","POST"])
def order_item_detail(order_item_id):
    return send_from_directory(order_item_bp.static_folder + '/detail', 'index.html')

# ------------------------------------------------------------------------------------

@order_item_bp.route('/api/list',methods=["POST"])
def api_order_item_list():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print(query)

    order_items = model.order_item_list(query)
    print('api 전송 직전',order_items['data'][0], order_items['paging'])
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(order_items)

