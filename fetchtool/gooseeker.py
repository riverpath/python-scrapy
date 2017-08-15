# _*_coding:utf-8_*_
from urllib import request
from urllib.parse import quote
from lxml import etree
import time

class GsExtractor(object):
    def _init_(self):
        self.xslt = ""
    # 从文件读取xslt
    def setXsltFromFile(self , xsltFilePath):
        file = open(xsltFilePath , 'r' , encoding='UTF-8')
        try:
            self.xslt = file.read()
        finally:
            file.close()
    # 从字符串获得xslt
    def setXsltFromMem(self , xsltStr):
        self.xslt = xsltStr
    # 通过GooSeeker API接口获得xslt
    def setXsltFromAPI(self , APIKey , theme, middle=None, bname=None):
        apiurl = "http://www.gooseeker.com/api/getextractor?key="+ APIKey +"&theme=" + quote(theme)
        if (middle):
            apiurl = apiurl + "&middle="+quote(middle)
        if (bname):
            apiurl = apiurl + "&bname="+quote(bname)
        apiconn = request.urlopen(apiurl)
        self.xslt = apiconn.read()
    # 返回当前xslt
    def getXslt(self):
        return self.xslt
    # 提取方法，入参是一个HTML DOM对象，返回是提取结果
    def extract(self , html):
        xslt_root = etree.XML(self.xslt)
        transform = etree.XSLT(xslt_root)
        result_tree = transform(html)
        return result_tree