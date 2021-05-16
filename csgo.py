# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:21:16 2021

@author: Administrator
"""

import pandas as pd
import requests 
import bs4


#创建新的空表
df = pd.DataFrame(index=[0])
df2 = pd.DataFrame(index=[0])



#爬地址
urls = ["https://www.hltv.org/results?offset={}".format(i) for i in range(0,3000,100)]
useragent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


for url in urls:
    #请求，得到整个网页源码
    r = requests.get(url,headers=useragent)
    #print(r.text)
    #用beautifulSoup解析
    soup = bs4.BeautifulSoup(r.text,'lxml')
    list1 = soup.find_all('a',class_='a-reset')
    for i in list1:
        data = pd.DataFrame(index=[1])
        data['名称'] = i.get('href')
        df =pd.concat([df,data])

df = df.drop(0)
df = df[df['名称'].str.contains("matches")].reset_index(drop=1)


for j in range(592,3426,1):
    r = requests.get("https://www.hltv.org"+df.名称[j],headers=useragent)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    data2 = pd.DataFrame(index=[1])
    data2['url'] = "https://www.hltv.org"+soup.find(class_='flexbox left-right-padding').get('href')
    df2 =pd.concat([df2,data2])


df2 = df2.drop(0)
df2.to_excel('D:/Python/jiJin/csgo.xlsx',index=False)
