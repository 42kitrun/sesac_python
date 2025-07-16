from flask import Flask, jsonify
import db.oracle as db
from user.user_route import user_bp
# from store.store_route import store_bp
# from item.item_route import item_bp
# from order.order_route import order_bp
# from order_item.order_item_route import order_item_bp

app = Flask(__name__)

# 앱에다 블루프린트를 등록한다.
app.register_blueprint(user_bp, url_prefix = '/user')
# app.register_blueprint(store_bp, url_prefix = '/store')
# app.register_blueprint(item_bp, url_prefix = '/item')
# app.register_blueprint(order_bp, url_prefix = '/order')
# app.register_blueprint(order_item_bp, url_prefix = '/order_item')

@app.route('/api/hello_world')
def api_hello_world():
    return jsonify('hello world')

@app.route('/')
def index():
    return jsonify('hello world')

if __name__ == '__main__':
    app.run(debug=True, port=7890)