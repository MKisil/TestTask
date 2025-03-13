from datetime import datetime, UTC
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.email}>'
