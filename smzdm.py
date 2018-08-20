# coding:utf-8

import os,sys
from bs4 import BeautifulSoup
from lxml import etree
import requests
import random
import re


def getContent(page=1):
    S = requests.Session()
    url = "https://www.smzdm.com/jingxuan/"
    url1 = "https://www.smzdm.com/jingxuan/p%d"
    target_url = ""
    if(page==1):
        target_url = url
    else:
        target_url = url1 % page
    headers = {
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':'text/html,application/xhtml-xml,application/xml,q=0.9,image/webp,*/*,q=0.8',
        'Referer':'https://www.smzdm.com/jingxuan',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Lanauage':'zh-CN,zh;q=0.8'
    }

    response = S.get(url=target_url,headers=headers)
    response.encoding = 'utf-8'

    target_html = response.text
    # htmlFormat = BeautifulSoup(target_html,'lxml')

    # content = BeautifulSoup(str(htmlFormat.find_all('li', class_='feed-row-wide')),'lxml')
    # info = content.li.contents
    print(target_html)


def readFile(file="2.log"):
    
    
    all = ""
    with open(file) as f:
        all = f.read()

    return all

def localRead(filecontent):
    
    
    soup = BeautifulSoup(filecontent, 'html.parser')

    tags = soup.find_all('li', class_="feed-row-wide")
    productList = []
    for tag in tags:
            # image = tag.img['src'] 图片地址
            h5_html = tag.find_all('h5',class_ = "feed-block-title")

            title = h5_html[0].get_text(strip=True)
            link = h5_html[0].a['href']
            temp = {}
            temp['title'] = title
            temp['link'] = link
            productList.append(temp)


    return productList


if __name__ == '__main__':
    # getContent(1)
    like = "音箱,收纳袋"
    content = localRead(readFile('data/2.log'))
    # if like in content:
    liktArr = like.split(',')
    for t in content:
        
        # print([str(ii) for ii in liktArr if ii in t['title']])//
        if([str(ii) for ii in liktArr if ii in t['title']]):
            print("%s#%s" % (t['title'],t['link']))
        # for i  in like.split(','):
            # print(i)
        # if (i in t['title'] for i  in like.split(',')):
            # print(t['title'])