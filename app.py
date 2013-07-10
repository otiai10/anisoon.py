# -*- coding: utf-8 -*-
from juno import *

@route('/')
def index(web):
    return '<h1>Hello, りっちゃん!!</h1><img src="http://oti10.com/public/src/favicon.jpg">'

run()
