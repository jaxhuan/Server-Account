import os
import sys
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command, Option
from flask_sqlalchemy import SQLAlchemy


# set gunicorn support to start with Flask-Script,bug:cannot use -D,so don't use.
class GunicornServer(Command):
    """Run the app within Gunicorn"""

    def get_options(self):
        from gunicorn.config import make_settings

        settings = make_settings()
        options = (
            Option(*kclass.cli)
            for setting, kclass in settings.items() if kclass.cli
        )

        return options

    def run(self, *args, **kwargs):
        run_args = sys.argv[2:]
        run_args.append('Account:app')
        os.execvp('gunicorn', [''] + run_args)


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
# manager.add_command('gunicorn', GunicornServer())
# use: python manager.py gunicorn -b 127.0.0.1:8000 -w 4 -D

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
