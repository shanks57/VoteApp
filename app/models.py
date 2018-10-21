from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Admin(db.Model):

    __tablename__ = 'adminpemilu'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(8))

    def get_id(self):

        return self.id

    @property
    def password(self):

        raise AttributeError('password is not readable attribute.')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):

        return '<Admin: {}>'.format(self.username)

class Pemilih(db.Model):

    __tablename__ = 'datapemilih'

    nim = db.Column(db.String(20), primary_key = True)
    nama = db.Column(db.String(20))
    password_hash = db.Column(db.String(8))
    status = db.Column(db.Boolean, default = False)

    def get_id(self):

        return self.nim

    @property
    def password(self):

        raise AttributeError('password is not readable attribute.')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):

        return '<Pemilih: {}>'.format(self.nim)

@login_manager.user_loader
def load_user(user_id):

    x = Admin.query.get(str(user_id))
    if x == None:
        x = Pemilih.query.get(str(user_id))
    return x
