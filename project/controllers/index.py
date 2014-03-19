# -*- coding: utf-8 -*-

from project import app
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash

from project.models.models import db
from project.models.user import User


@app.endpoint('index')
def index():
    return render_template('index.html')
