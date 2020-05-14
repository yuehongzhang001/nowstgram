# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)
app.secret_key = 'nowcoder'
login_manager = LoginManager(app);

from nowstgram import views,models


from sqlalchemy import Column, Integer, String
Column()