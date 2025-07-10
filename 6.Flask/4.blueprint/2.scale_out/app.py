from flask import Flask,render_template
from user.user_route import user_bp
from admin.admin_route import admin_bp
from product.product_route import product_bp

app = Flask(__name__)

# 앱에다 블루프린트를 등록한다.
app.register_blueprint(user_bp, url_prefix = '/user')
app.register_blueprint(admin_bp, url_prefix = '/admin')
app.register_blueprint(product_bp, url_prefix = '/product')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=7890)