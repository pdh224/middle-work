from datetime import datetime
from apps.app import db

from werkzeug.security import generate_password_hash, check_password_hash

class talk(db.Model):
    __tablename__="talk"
    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, index=True)
    massage= db.Column(db.String,unique=True, index=True)
    # password_hash=db.Column(db.String)
    # created_at=db.Column(db.DateTime, default=datetime.now)
    # updated_at= db.Column(
    #     db.DateTime, default=datetime.now, onupdate=datetime.now
    #)

    # 속성값 getter
    # @property
    # def password(self):
    #     raise AttributeError("읽어 들일 수 없음")
    
    # @password.setter
    # def password(self, password):
    #     self.password_hash=generate_password_hash(password)


    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash,password)
    # def is_duplicate_email(self):
    #     return User.query.filter_by(email=self.email).first() is not None
    
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(user_id)