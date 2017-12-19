
import urllib.request;

import re;

import random;

def getHtml(url):
    webPage=urllib.request.urlopen(url)
    html=webPage.read()
    return html


def getImg(html):
    reg=r'src="http(.+?\.png)"'
    imgre=re.compile(reg)
    html1=html.decode('utf-8')
    imgList=re.findall(imgre,html1)

    return imgList


def local(list):
    x=1
    print(list)
    for imgUrl in list:
        imgUrl='http'+imgUrl
        
        saved_pic = "C:\\Users\\admin\\Pictures\\Camera Roll\\imgs\\"    
        saved_pic +=str(x)+'.png'
        urllib.request.urlretrieve(imgUrl,saved_pic)
        x+=1

url="http://www.yopark.com/";

html =getHtml(url)

list=getImg(html)

local(list)





