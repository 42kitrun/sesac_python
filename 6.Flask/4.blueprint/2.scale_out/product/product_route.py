from flask import Blueprint,render_template

product_bp = Blueprint('product', __name__, template_folder = '../templates/product')

@product_bp.route('/')
def product():
    return render_template('product.html')

@product_bp.route('/')
def fruit():
    return render_template('fruit.html')

@product_bp.route('/')
def drink():
    return render_template('drink.html')