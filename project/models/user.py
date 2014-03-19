# -*- coding: utf-8 -*-

from project.models.models import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    pw_hash = db.Column(db.String(32), nullable=False)
