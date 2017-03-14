from . import web
from flask import render_template


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/cover')
def cover():
    return render_template('cover.html')
