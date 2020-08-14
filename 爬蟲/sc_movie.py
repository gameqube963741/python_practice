# import ssl 
# ssl._create_default_https_context = ssl._create_unverified_context
# # from urllib import request
# import requests
# from bs4 import BeautifulSoup

# #headers

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
# headers = {'User-Agent': user_agent}

# url = 'https://www.ptt.cc/bbs/joke/index.html'
# res = requests.get(url, 'html.parsrt')

# soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup.prettify())

# article_title_html = soup.select('div[class="title"]')
# # print(article_title_html)

# # 找標籤
# for each_article in article_title_html:
#     print(each_article.a.text)
#     print('https://www.ptt.cc'+ each_article.a['href'])
#     print()

# # 印出文章標題後要進入上一頁，找到標籤位置
# last_page_url = soup.select('div[class="btn-group btn-group-pagong"]')[0].select('a')[1]['href']
# last_page_url = 'https://www.ptt.cc' + last_page_url

# url = last_page_url

import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

import requests
from bs4 import BeautifulSoup

#headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
}

for i in range(0,3):
    url = 'https://www.ptt.cc/bbs/joke/index.html'

    res = requests.get(url, 'html.parsrt')

    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    # 找標籤
    for each_article in article_title_html:
        print(each_article.a.text)
        print('https://www.ptt.cc'+ each_article.a['href'])
        print()

    # 印出文章標題後要進入上一頁，找到標籤位置
    last_page_url = soup.select('div[class="btn-group btn-group-pagong"]')[0]\
                        .select('a')[1]['href']
    last_page_url = 'https://www.ptt.cc' + last_page_url
    url = last_page_url