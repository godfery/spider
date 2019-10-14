# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import subprocess as sp
from lxml import etree
import requests
import random
import re
import json

"""
函数说明:获取IP代理
Parameters:
    page - 高匿代理页数,默认获取第一页
Returns:
    proxys_list - 代理列表
Modify:
    2017-05-27
"""
def get_proxys(page = 1):
    #requests的Session可以自动保持cookie,不需要自己维护cookie内容
    S = requests.Session()
    #西祠代理高匿IP地址
    target_url = 'http://127.0.0.1/top.html'
    #完善的headers
    target_headers = {'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':'http://www.xicidaili.com/nn/',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
    }
    #get请求
    target_response = S.get(url = target_url, headers = target_headers)
    #utf-8编码
    target_response.encoding = 'utf-8'
    #获取网页信息
    target_html = target_response.text
    # #获取id为ip_list的table
    bf1_ip_list = BeautifulSoup(target_html, 'lxml')
    # print(bf1_ip_list)
    bf2_ip_list = BeautifulSoup(str(bf1_ip_list.find_all(class_="cc-cd-cb nano")), 'lxml')

    # print(bf2_ip_list.contents)
    bf3_ip_list = BeautifulSoup(str(bf2_ip_list.find_all(class_="cc-cd-cb-l nano-content")), 'lxml')

    # print(bf3_ip_list.div.contents)
   
    ip_list_info = bf3_ip_list.contents
    # #存储代理的列表
    content_lists = []

    # #爬取每个代理信息

    for index in range(len(ip_list_info)):
        # if index % 2 == 1 and index != 1:
        dom = etree.HTML(str(ip_list_info[index]))
        # print(str(ip_list_info[index]))
        if dom != None:
            a = dom.xpath('//a')
            count =0
            tempStr = ""
            for i in a:
                # print(etree.tostring(i, encoding="utf-8", pretty_print=True).decode("utf-8"))

                
                tempStr = tempStr +  i.attrib['href'] + ";"
                sibling_soup = BeautifulSoup(etree.tostring(i, encoding="utf-8", pretty_print=True).decode("utf-8"))
                spanTemp = sibling_soup.find_all('span')
                for jj in spanTemp:
                    tempStr = tempStr +  jj.text + ";"
                content_lists.append(tempStr)
         
    # #返回列表
    print(content_lists)


if __name__ == '__main__':
    
    get_proxys(1)

    