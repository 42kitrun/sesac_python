from flask import Flask, jsonify
from db.oracle import OracleDBPool
from user.route import user_bp
# from store.store_route import store_bp
# from item.item_route import item_bp
# from order.order_route import order_bp
# from order_item.order_item_route import order_item_bp
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.


def create_app(): 
    OracleDBPool.init_pool()  # 커넥션 풀 초기화 (최초 1회만 실행) 커넥션 풀 싱글톤 클래스

    # 앱에다 블루프린트를 등록한다.
    app.register_blueprint(user_bp, url_prefix = '/user')
    # app.register_blueprint(store_bp, url_prefix = '/store')
    # app.register_blueprint(item_bp, url_prefix = '/item')
    # app.register_blueprint(order_bp, url_prefix = '/order')
    # app.register_blueprint(order_item_bp, url_prefix = '/order_item')
    return app

print('인터넷이 안되면 oracle db와의 연결 때문에 안 올라옵니다')
app = create_app()

'''
- create_app() : 앱이 켜질 때 딱 한 번!
- @app.before_first_request : 앱 실행 후 첫 요청 들어올 때 늦게 초기화 필요할 때
  커넥션 풀 같은 건 미리 켜두는 게 안정적
- @app.before_request : 요청마다 실행
  커넥션 풀 생성같이 무거운 작업은 하면 안 됨
'''

@app.route('/api/hello_world')
def api_hello_world():
    return jsonify('hello world')

@app.route('/')
def index():
    return jsonify('hello world')

if __name__ == '__main__':
    app.run(debug=True, port=7890)