from sqlalchemy.ext.hybrid import hybrid_property
from . import db, bcrypt
import json


class User(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    _password = db.Column(db.String(128))
    token = db.Column(db.String(128), unique=True, default='')

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = bcrypt.generate_password_hash(pwd)

    def is_current_pwd(self, pwd):
        if bcrypt.check_password_hash(self._password, pwd):
            return True
        return False

    def toDict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__toDict(), ensure_ascii=False, separators=(',', ':'))
