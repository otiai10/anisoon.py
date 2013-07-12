import requests,urllib

def search(anime):
    for t in anime['music']['op']:
        query(t)
    for t in anime['music']['ed']:
        query(t)

def query(s):
    url = 'http://gdata.youtube.com/feeds/api/videos'
    url = url + '?alt=json'
    url = url + '&max-results=1'
    # url = url + '&category=music'
    url = url + '&category=Anime'
    url = url + '&q=' + s
    r = requests.get(url)
    jsn = r.json()
    print '-------------------------------'
    print url
    try:
        for v in jsn['feed']['entry']:
            print v
    except:
        pass
    #return r.json()
