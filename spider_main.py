import html_outputer
import html_downloader
import html_parser
import url_manager


#爬行调度程序
# class SpiderMain(object):
#     def __int__(self):
#         self.urls       = url_manager.UrlManager()
#         self.downloader = html_downloader.HtmlDownloader()
#         self.paser      = html_parser.HtmlPaser()
#         self.outputer   = html_outputer.HtmlOutputer()
#
#
#     def craw(self, root_url):
#         count = 1   #记录当前爬行的是第几个url
#         self.urls.add_new_url(root_url)
#         while self.urls.has_new_url():
#
#             try:
#                 new_url = self.urls.get_new_url()
#
#                 print('craw %d : %s' % (count, new_url))
#
#                 html_cont = self.downloader.download(new_url)
#                 new_urls, new_data = self.paser.parse(new_url, html_cont)   #当前爬取的url和下载好的页面数据
#                 self.urls.add_new_urls(new_urls)
#                 self.outputer.collect_data()
#
#                 if count == 1000:
#                     break
#
#                 count = count + 1
#             except:
#                 print('爬取错误')
#
#
#         self.outputer.output_html() #输出梳理好的数据
#
#
#
# if __name__ == "__main__":
#     root_url = "http://baike.baidu.com/view/21087.htm"
#     obj_spider = SpiderMain()
#     obj_spider.craw(root_url)


#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 爬虫调度端

## URL管理器

### 添加新的URL到待爬取集合中
### 判断待添加URL是否在容器中
### 获取待爬取URL
### 判断是否还有待爬取URL
### 将URL从待爬取移动到已爬取

## 网页下载器
### urllib2
### requests

## 网页解析器

### 正则表达式
### html.parser
### BeautifulSoup
### lxml


## 分析目标
### URL格式
### 数据格式
### 网页编码




class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()



    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


                if count == 1000:
                    break
                count = count + 1
            except:
                print('craw failed')

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
