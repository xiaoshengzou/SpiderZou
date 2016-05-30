# coding:utf8

import urllib2

class HtmlDownload(object):
    """docstring for HtmlDownload"""

    def download(self, url):
        if url is None:
            return None
        responce = urllib2.urlopen(url)

        print responce.getcode()

        if responce.getcode() != 200:
            return None
        return responce.read()
