from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return 'User %r' % self.username

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }