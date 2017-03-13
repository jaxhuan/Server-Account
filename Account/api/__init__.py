from flask import Blueprint

api = Blueprint('api', __name__)

# 定义api之后才导入views,因为views需要使用api
from . import views
