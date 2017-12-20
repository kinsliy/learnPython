
import urllib.request;

import re;
import json

import random;

def getHtml(url):
    webPage=urllib.request.urlopen(url)
    html=webPage.read()
    print(html)
    #data = json.loads(html)
    #print(data)
    #return data


def getImg(html):
    reg=r'src="https(.+?\.jpeg|jpg|png)"'
    imgre=re.compile(reg)
    html1=html.decode('utf-8')
    imgList=re.findall(imgre,html1)
    print(imgList)
    return imgList


def local(list):
    x=1
   
    for imgUrl in list['imgs']:
        #imgUrl='http'+imgUrl
        
        saved_pic = "C:\\Users\\admin\\Pictures\\Camera Roll\\imgs\\"    
        saved_pic +=str(x)+'.png'
        urllib.request.urlretrieve(imgUrl['objURL'],saved_pic)
        x+=1

url="https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B9%F9%B1%CC%E6%C3&fr=ala&ala=1&alatpl=star&pos=0&hs=2&xthttps=111111";

html =getHtml(url)

#list=getImg(html)

#local(html)

#正则匹配需要注意以及写入本地的那个函数，坑





