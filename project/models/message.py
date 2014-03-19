# -*- coding: utf-8 -*-

from project.models.models import db


class Message(db.Model):
    __tablename__ = 'message'

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(140), nullable=False)
    pub_date = db.Column(db.Integer, default=db.func.now(), onupdate=db.func.now())
    #pub_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
