import requests
url = 'http://www.ehappy.tw/demo.htm'
r = requests.get(url)

if r.status_code == requests.codes.ok:
    print(r.text) 