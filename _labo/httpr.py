# -*- coding: utf-8 -*-
import requests,json,time,re

r = requests.get('http://cal.syoboi.jp/json.php?Req=TitleFull&Start=2013-06-02')

jsn = r.json()

def dump_list(l):
    if l is not None:
        for v in l:
            mtitle = extract_mtitle(v[:-2])
            if mtitle is not None:
                print mtitle

def extract_mtitle(s):
    pat = u'「.*」'
    match = re.search(pat,s)
    if match is None:
        return None
    return match.group(0)[1:-1]

for r in jsn['Titles'].items():
    v   = r[1]
    com = v['Comment']
    pat_op = u'オープニングテーマ.*\n'
    pat_ed = u'エンディングテーマ.*\n'
    match_op = re.findall(pat_op,com,re.U)
    match_ed = re.findall(pat_ed,com,re.U)
    # {{{ -------------------------------- Filter ------------------------
    if int(v['Cat']) is not 1:
        continue
    if v['FirstYear'] is None:
        continue
    if int(v['FirstYear']) < 2013:
        continue
    # }}}
    print '----- TID : ', r[0], '------------------------------------------------------------'
    print "Title\t%s\tTID\t%s\tCat\t%s" % (v['Title'],v['TID'],v['Cat'])
    print "FirstYear\t%s\tFristCh\t%s" % (v['FirstYear'],v['FirstCh'])
    print '*********', pat_op[:-3], '*********'
    dump_list(match_op)
    print '*********', pat_ed[:-3], '*********'
    dump_list(match_ed)
