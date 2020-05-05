# -*- encoding=UTF-8 -*-

from nowstgram import app

@app.route('/')
def index():
    return 'Hello,index!'