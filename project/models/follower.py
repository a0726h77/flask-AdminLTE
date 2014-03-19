# -*- coding: utf-8 -*-

from project.models.models import db


class Follower(db.Model):
    __tablename__ = 'follower'

    who_id = db.Column(db.Integer, primary_key=True)
    whom_id = db.Column(db.Integer, primary_key=True)
