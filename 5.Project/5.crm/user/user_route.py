import sys
sys.path.append('5.Project/5.crm')

from flask import Blueprint,render_template,jsonify
import db.oracle as db

user_bp = Blueprint('user', __name__, template_folder = '../templates/user')

@user_bp.route('/list')
def user_list():
    return render_template('users.html')

@user_bp.route('/api/list')
def api_user_list():
    users = db.get_users()
    return jsonify(users)