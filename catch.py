#coding:utf-8
import  urllib
import re
import urllib2 as ulb
from bs4 import BeautifulSoup

# def get_html(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

## 模拟谷歌浏览器

my_header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36";

#定义每日问题url接口

every_date = "https://github.com/Advanced-Frontend/Daily-Interview-Question/issues/"


def get_html(url):
    response = ulb.Request(url)
    print response
    response.add_header('User-Agent', my_header)
    page = ulb.urlopen(response);
    html = page.read();
    soup = BeautifulSoup(html,'lxml')
    print soup;
    return html


pageFile = open('./pageCode.html','w') 
pageFile.write(get_html("http://github.com/Advanced-Frontend/Daily-Interview-Question"))
pageFile.close()



print re.findall(every_date, "href='https://github.com/Advanced-Frontend/Daily-Interview-Question/issues/123'")
