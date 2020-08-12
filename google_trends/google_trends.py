#pip install pytrends
from pytrends.request import TrendReq

pytrends = TrendReq(hl='tw-TW', tz=360)
trends = pytrends.trending_searches(pn='taiwan')
trends_values = trends.values.tolist()
google_trend_list = []
for value in trends_values:
    item = str(value[0])
    item = item.replace('　', '')
    item = item.replace(' ', '')
    google_trend_list.append(item)
print('google_trend_list = ' + str(google_trend_list))


# 查询期间指定：
timeframe='now 1-d' #-> 過去一天
timeframe='today 1-m' #-> 過去一個月
timeframe='today 5-y' #-> 過去五年

KEYWORD = '米中'
kw_list = [KEYWORD]
pytrends.build_payload(kw_list, cat=0, timeframe='now 1-d', geo='TW', gprop='')
trends = pytrends.related_queries()
trends_values = trends[KEYWORD]['top'].values.tolist()

#pip install wordcloud
from collections import Counter
from wordcloud import WordCloud
# ---------- 出圖設定 ----------
WORDCLOUD_FONT_PATH = '/Users/edward/Library/Fonts/TaipeiSansTCBeta-Light.ttf'
WORDCLOUD_WIDTH = 600
WORDCLOUD_HEIGHT = 600
WORDCLOUD_BG_COLOR = 'white'
WORDCLOUD_OUTPUT_FILE = './wordcloud.png'
word_counter = Counter(google_trend_list)
wordcloud = WordCloud(
    font_path = WORDCLOUD_FONT_PATH,
    width = WORDCLOUD_WIDTH,
    height = WORDCLOUD_HEIGHT,
    background_color = WORDCLOUD_BG_COLOR,
    colormap="summer").generate_from_frequencies(word_counter)
wordcloud.to_file(WORDCLOUD_OUTPUT_FILE)