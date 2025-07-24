from flask import Blueprint,send_from_directory,jsonify,request
import be.store.model as model

store_bp = Blueprint('store', __name__
                                    # , root_path=os.path.abspath(os.path.dirname(__file__ + "/../.."))
                                    , root_path='/Users/seSAC/src/sesac_python/5.Project/5.crm'
                                    , static_folder = 'fe/static/store'   # 실제 파일(하드디스크, 코드상 폴더) 위치
                                    , static_url_path = '/fe/static/store' # 브라우저에서 접근할 때 사용할 URL 주소(URL(주소창)은 웹 서버의 루트(/)를 기준)
)

@store_bp.route("/", methods=["GET","POST"])
def store():
    return send_from_directory(store_bp.static_folder + '/list', 'index.html')

## store/detail/0a497257-2b1a-4836-940f-7b95db952e61/?listCount=10&page=3
@store_bp.route("/<uuid:store_id>", methods=["GET", "POST"])
def store_detail(store_id):
    return send_from_directory(store_bp.static_folder + '/detail', 'index.html')

# ------------------------------------------------------------------------------------

@store_bp.route('/api/list',methods=["POST"])
def api_store_list():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print(query)

    stores = model.store_list(query)
    print('api 전송 직전',stores['data'][0], stores['paging'])
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(stores)


#store_detail_api이지만 실상 order table이 drive table이라면...? 어떻게 라우트를 설계해야하나...?
# store/api/loyalty? order/api/loyalty?
@store_bp.route('/api/monthly_sales',methods=["POST"])
def api_store_sales_monthly():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print('/store/api/monthly_sales',query)

    sales_monthly = model.store_sales_monthly(query)
    print('api 전송 직전',sales_monthly['data'][0], sales_monthly['paging'])
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(sales_monthly)

@store_bp.route('/api/loyalty', methods=["POST"])
def api_store_loyalty():
    query = dict(request.form) # post로 보낸거는 request.from // get으로 보낸거는 request.args
    print('/store/api/loyalty',query)

    loyalty = model.store_loyalty(query)
    print('api 전송 직전',loyalty['data'][0], loyalty['paging'])
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    return jsonify(loyalty)