# -*- encoding=UTF-8 -*-

from nowstgram import app, db
from models import Image,User,Comment
from flask import render_template, redirect,request, flash, get_flashed_messages
import random, hashlib


@app.route('/')
def index():
    images = Image.query.order_by(Image.id.desc()).limit(10).all()
    return render_template('index.html', images=images)

@app.route('/image/<image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    if image == None:
        return redirect('/')
    return render_template('pageDetail.html', image=image)

@app.route('/profile/<user_id>')
def profile(user_id):
    user = User.query.get(user_id)
    if user == None:
        return redirect('/')
    return render_template('profile.html', user=user)

@app.route('/regloginpage')
def regloginpage():
    msg = ''
    for m in get_flashed_messages(with_categories=False, category_filter=['reglogin']):
        msg = msg + m
    return render_template('login.html', msg=msg)

def redirect_with_msg(target,msg,category):
    if msg != None:
        flash(msg, category=category)
    return redirect(target)


@app.route('/reg/', methods={'post','get'})
def reg():
    username=request.values.get('username').strip()
    password = request.values.get('password').strip()
    # check if the username is empty
    if username == '' or password == '':
       return redirect_with_msg('/regloginpage',u'用户名或密码不能为空',category='reglogin')

    #check if the username exists or not
    user = User.query.filter_by(username=username).first()
    if user != None:
        return redirect_with_msg('/regloginpage',u'用户名已存在',category='reglogin')

    # create the user and store it in the database
    salt = '.'.join(random.sample('0123456789abcdefghijklmnopqrstuvwxyz',10))
    m = hashlib.md5()
    m.update(password+salt)
    password = m.hexdigest()
    user = User(username,password,salt)
    db.session.add(user)
    db.session.commit()

    #redirect to the index page
    return redirect('/')