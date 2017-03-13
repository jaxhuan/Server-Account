from . import api
from ..models import User, db
from flask import request, jsonify


def make_result(code=1, msg='', data=''):
    return jsonify({'ok': code, 'msg': msg, 'data': data})


@api.route('/')
def index():
    return 'Hello,Account Api'


@api.route('/users')
def get_users():
    users = User.query.all()
    list_user = [user.toDict() for user in users]
    return make_result(data=list_user)


@api.route('/register', methods=['POST'])
def register():
    user = User()
    user.username = request.form['username']
    user.password = request.form['password']
    db.session.add(user)
    db.session.commit()
    return make_result()


@api.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(username=request.form['username']).first()
    result_dict = {'ok': 1, 'msg': '', 'data': user.is_current_pwd(request.form['password'])}
    return make_result(data=user.is_current_pwd(request.form['password']))
