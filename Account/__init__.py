from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from .api import api
from .web import web

# Blueprint 初始化
# subdomain为子域名(必须设置SERVER_NAME),而url_prefix为该蓝图的前缀
# app.register_blueprint(api, subdomain='api')
app.register_blueprint(api, url_prefix='/account/api')

# app.register_blueprint(web, subdomain='web')
app.register_blueprint(web, url_prefix='/account/web')


# @app.before_first_request
# def create_database():
#     db.create_all()
