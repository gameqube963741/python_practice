import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
from urllib import request
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/joke/index.html'

#headers
# useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
# header = {'Useragent' :useragent}
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
headers = {'User-Agent': user_agent}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

# print(res.read().decode('utf-8-sig'))

soup = BeautifulSoup(res, 'html.parser')
# action_bar = soup.findAll('div', {'id':'action-bar-container'})
action_bar = soup.select('div[id="action-bar-container"]')
print(action_bar)

# try to get other <div> tag and <a> and in action_bar
tmp_div = action_bar[0].div
# print('Other <div>:')
# print(tmp_div)
# print()

tmp_a = action_bar[0].a
# print('Other <a>:')
# print(tmp_a)

# get text in tag
tmp_text_in_a = tmp_a.text
# print('Text in <a> tag:')
# print(tmp_text_in_a)
# print()

# get url in <a> tag
# tmp_url = tmp_a['href']
# print('URL:')
# print(tmp_url)
# print()
# print('https://www.ptt.cc'+tmp_url)

