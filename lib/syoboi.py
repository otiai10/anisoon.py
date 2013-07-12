# -*- coding: utf-8 -*-
import requests,json,time,re

def get_mtitle_list(l):
    mtitle_list = []
    if l is not None:
        for v in l:
            mtitle = extract_mtitle(v[:-2])
            if mtitle is not None:
                mtitle_list.append({'mtitle':mtitle})
    return mtitle_list

def extract_mtitle(s):
    pat = u'「.*」'
    match = re.search(pat,s)
    if match is None:
        return None
    return match.group(0)[1:-1]

def filtered(anime):
    if int(anime['Cat']) is not 1:
        return 1
    if anime['FirstYear'] is None:
        return 1
    if int(anime['FirstYear']) < 2013:
        return 1
    return 0
 

def search(date):

    r = requests.get('http://cal.syoboi.jp/json.php?Req=TitleFull&Start=2013-06-02')
    jsn = r.json()

    _list = []

    for r in jsn['Titles'].items():

        if filtered(r[1]): continue

        v   = r[1]
        com = v['Comment']
        pat_op = u'オープニングテーマ.*\n'
        pat_ed = u'エンディングテーマ.*\n'
        match_op = re.findall(pat_op,com,re.U)
        match_ed = re.findall(pat_ed,com,re.U)
        v['music'] = {}
        v['music']['op'] = get_mtitle_list(match_op)
        v['music']['ed'] = get_mtitle_list(match_ed)

        _list.append(v)

    return _list

if __name__ == '__main__':
    anime_list = search('2013-06-02')
    for anime in anime_list:
        print '----'
        print anime
