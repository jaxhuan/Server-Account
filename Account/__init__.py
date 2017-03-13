from flask import Flask
from .api import api
from .web import web
from .models import db, bcrypt

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Blueprint 初始化
# subdomain为子域名(必须设置SERVER_NAME),而url_prefix为该蓝图的前缀
# app.register_blueprint(api, subdomain='api')
app.register_blueprint(api, url_prefix='/account/api')

# app.register_blueprint(web, subdomain='web')

db.init_app(app)
bcrypt.init_app(app)


@app.before_first_request
def create_database():
    db.create_all()
