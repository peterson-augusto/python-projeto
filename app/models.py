from app.database import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from main import ma


@login_manager.user_loader
def get_user(user_id):
    return Users.query.filter_by(id=user_id).first()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(70), nullable=True)
    l_name = db.Column(db.String(70), nullable=True)
    email = db.Column(db.String(30), unique=True)
    gender = db.Column(db.String(30))
    birthdata = db.Column(db.Date)
    password = db.Column(db.String, nullable=False)
    
    def __init__(self, f_name, l_name, email, gender, birthdata, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.gender = gender
        self.birthdata = birthdata
        self.password = generate_password_hash(password)
        
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
    
db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email', 'gender', 'birthdata', 'password')
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)