# coding:utf8

import url_manage
import html_download
import html_parser
import output

class SpiderMain(object):
    """docstring for SpiderMain
    """
    def __init__(self):
        self.urls          = url_manage.UrlManage()
        self.html_download = html_download.HtmlDownload()
        self.html_parser   = html_parser.HtmlParser()
        self.output        = output.OutPut()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_url():
            try:
                new_url = self.urls.get_new_url()
                print 'No.%d url:%s' % (count, new_url)
                html_cont= self.html_download.download(new_url)

                new_urls,new_data=self.html_parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print 'craw fiald!'
        self.output.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    spider = SpiderMain()
    spider.craw(root_url)