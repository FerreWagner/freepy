
#爬行调度程序
class SpiderMain(object):
    def __int__(self):
        self.urls       = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.paser      = html_parser.HtmlPaser()
        self.outputer   = html_output.HtmlOutputer()

    def craw(self, root_url):
        count = 1   #记录当前爬行的是第几个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():

            try:
                new_url = self.urls.get_new_url()

                print('craw %d : %s'%(count, new_url))

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.paser.parse(new_url, html_cont)   #当前爬取的url和下载好的页面数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data()

                if count == 1000:
                    break

                count = count + 1
            except:
                print('爬取错误')


        self.outputer.output_html() #输出梳理好的数据



if __name__ == "__main__":
    root_utl = "https://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
