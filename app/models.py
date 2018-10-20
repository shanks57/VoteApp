#import extension and third-party
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


#local import
from app import db,login_manager


class AdminPemilu(db.Model):

    __tablename__ = 'adminpemilu'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(20))

    #get user_id untuk admin
    def get_id(self):

        return self.id

    @property

    def password(self):

        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self,password):

        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):

        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<AdminPemilu: {}>'.format(self.username)


class DataPemilih(db.Model):

    nim = db.Column(db.Sring(25), primary_key = True)
    password = db.Column(db.String(20))

    # get user_id untuk pemilih
    def get_id(self):
        return self.nim

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<DataPemilih: {}>'.format(self.username)




#set up user_loader
@login_manager.user_loader()
def load_user(user_id):

    x = AdminPemilu.query.get(str(user_id))
    if x == None:

        x = DataPemilih.query.get(str(user_id))

    return x


