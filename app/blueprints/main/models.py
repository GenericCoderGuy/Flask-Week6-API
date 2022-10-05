from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# association_table = Table(
#     "association",
#     db.Model.metadata,
#     parent = db.Column("user_id", db.ForeignKey("user.id")),
#     child = db.Column("user_id", db.ForeignKey("user.id")),
# )

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    pokemons = db.relationship("Pokemon", back_populates="user")

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(1200))
    type = db.Column(db.String(256))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="pokemons")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)