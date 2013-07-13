# -*- coding: utf-8 -*-
from juno import *
import lib
from datetime import date, datetime, timedelta
import json

@route('/')
def index(web):
    month_ago = date.today() - timedelta(30)
    from_date = '%s-%s-%s' % (month_ago.year, month_ago.month, month_ago.day)
    anime_list = lib.syoboi.search(from_date)
    return template('index.html', { 'list': json.dumps(anime_list), 'date':from_date })

@route('/favicon.ico')
def favicon(web):
    return 'Action Undefined...'

@route('/:anypath')
def undefined(web, anypath):
    return '(☝ ՞ਊ ՞)☝ｳｪｰｲ<br><a href="/">HOME</a>'

run()
