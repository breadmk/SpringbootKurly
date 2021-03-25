import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
driver=webdriver.Chrome('data\\chromedriver.exe')
with open(os.path.join('data','자주.csv'),'w',encoding='utf-8') as f:
    for i in range(1,6):
        url='https://www.kurly.com/shop/service/faq.php?page=%d'%(i)
        driver.get(url)
        # print(dom)
        # divs=dom.find_all('div',class_="xans-element- xans-myshop xans-myshop-couponserial ")
        for j in range(1,16):
            divs1 = driver.find_element_by_css_selector("#form > div > div.xans-element-.xans-myshop.xans-myshop-couponserial > div:nth-child(2) > div:nth-child(%d) td:nth-child(2)"%(j)).text
            divs2 = driver.find_element_by_css_selector("#form > div > div.xans-element-.xans-myshop.xans-myshop-couponserial > div:nth-child(2) > div:nth-child(%d) td:nth-child(3)"%(j)).text
            print(divs)
            for k in divs:
                print(k)
            td= divs[3].text
            print(td)
            f.write(divs1+" "+divs+'\n')
# 워드클라우드 시각화
with open('data/자주.csv', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
lines = text.split('\n')

worddic = {}
for line in lines:
    mal = okt.pos(line, norm=True, stem=True)
    for m in mal:
        if len(m[0]) > 1 and m[1] == 'Noun' and m[0] not in stopwords:
            if not(m[0] in worddic):
                worddic[m[0]] = 0
            worddic[m[0]] = worddic[m[0]] + 1
dic = dict(sorted(worddic.items(), key=lambda x: x[1], reverse=True)[:100])
wc = WordCloud(font_path='malgun.ttf',background_color='white').generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()
#
