# -*- coding: utf-8 -*-
from juno import *
import lib
from datetime import date, datetime, timedelta
import json

@route('/')
def index(web):
    three_days_ago = date.today() - timedelta(3)
    print '%s-%s-%s' % (three_days_ago.year, three_days_ago.month, three_days_ago.day)
    anime_list = lib.syoboi.search('2013-06-30')
    return template('index.html', { 'list': json.dumps(anime_list) })

@route('/favicon.ico')
def undefined(web):
    return 'Action Undefined...'

run()
