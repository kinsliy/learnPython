
import urllib.request;

import re;

def getHtml(url):
    webPage=urllib.request.urlopen(url)
    html=webPage.read()
    return html


baiduUrl='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111111&sf=1&fmq=1513667534350_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%BD%98%E6%BD%87%E6%BD%87&oq=%E6%BD%98%E6%BD%87%E6%BD%87&rsp=-1'

def getImg(html):
    reg=r'src="(.+?\.[jpg|png])"'
    img=re.compile(reg)

    imgList=re.findall(img,html)

    x=0;

    for imgUrl in imgList:
        # urllib.request.urlretrieve('new.jpg'%x)
        # x+=1
        print(imgUrl)

    
html =getHtml(baiduUrl)

getImg(html)

print('233')






