#coding=utf-8
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient, HTTPError
from tornado.httpclient import HTTPRequest
import requests,re,json,time
import pandas as pd
import numpy as np
from lxml import etree
import codecs



URLS = ["http://data.stats.gov.cn/search.htm?s=CPI&m=searchdata&db=&p=" + str(i) for i in range(21)]
with open('cookie.txt','r') as f:
    cookie_data=f.read()
class MyClass(object):

    def __init__(self):
        #AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        self.http = AsyncHTTPClient()
        self.data_total=[]
        self.headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
   'Accept-Language': 'zh-CN,zh;q=0.8',
   'Accept-Encoding': 'gzip, deflate',"Cookie" : cookie_data}
    @coroutine  
    def get(self, url):
        #tornado会自动在请求首部带上host首部        
        request = HTTPRequest(url=url,
                            method='GET',
                            headers=self.headers,
                            connect_timeout=300.0,
                            request_timeout=600.0,
                            follow_redirects=False,
                            max_redirects=False,
                            user_agent="Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36",)
        yield self.http.fetch(request, callback=self.find, raise_error=False)
    def set_pstr(self,pstr):
        self.pstr=pstr
    def set_header(self,headers):
        self.headers=headers
    def find(self, response):
        if response.error:
            # print(response.error)
            pass
        # tree=etree.HTML(response.body.decode('gbk','ignore'))
        # a=tree.xpath('//a[@offer-stat="com"]/text()')
        # print(a)
        try:
            tree=etree.HTML(response.body.decode('gbk','ignore'))
            a=tree.xpath('//a[@offer-stat="com"]/text()')
            b=tree.xpath('//a[@offer-stat="com"]/@href')
            if tree!=None:
                self.data_total.append(pd.DataFrame([{'企业名称':a[i].strip(),'URL':b[i].strip() + "/page/contactinfo.htm"} for i in range(len(a))],index=range(len(a))))
        except:
            # print("error")
            pass
    def savefile(self, response):
        if response.error:
            print(response.error)
        print(response.code, response.effective_url, response.request_time )
        try:
            code=re.search(r'code=(.*?)&',response.effective_url)[1]
            pat=re.compile(r"(\[\[.*?\]\])",re.S)
            m=pat.search(response.body.decode('utf-8'))
            tt=json.loads(m.group(1))
            columns=[u"日期",u"开盘价",u"最高价",u"收盘价",u"最低价",u"成交量",u"涨跌额",u"涨跌幅",u"5日均价",u"10日均价",u"20日均价",u"5日均量",u"10日均量",u"20日均量",u"换手率"]
            frame=DataFrame(tt,columns=columns)
            frame[[u"开盘价",u"最高价",u"收盘价",u"最低价",u"成交量",u"涨跌额",u"涨跌幅",u"5日均价",u"10日均价",u"20日均价",u"换手率"]]=frame[[u"开盘价",u"最高价",u"收盘价",u"最低价",u"成交量",u"涨跌额",u"涨跌幅",u"5日均价",u"10日均价",u"20日均价",u"换手率"]].astype(float)
            frame[u"5日均量"]=frame[u"5日均量"].str.replace(',','').astype(float)
            frame[u"10日均量"]=frame[u"10日均量"].str.replace(',','').astype(float)
            frame[u"20日均量"]=frame[u"20日均量"].str.replace(',','').astype(float)
            frame.set_index([u'日期']).to_csv(code +'.csv')        
        except:
            print("error")    
        
class Download(object):

    def __init__(self):
        self.a = MyClass()
    def set_url(self,urls):
        self.urls = urls
    @coroutine
    def d(self):
        print(r'基于tornado的并发抓取')        
        t1 = time.time()
        yield [self.a.get(url) for url in self.urls]
        t = time.time() - t1
        print(t)

    def data_concat(self,urls,pstr):
        self.set_url(urls)
        self.a.set_pstr(pstr)
        loop = IOLoop.current()
        loop.run_sync(self.d)
        self.data_total=pd.concat(self.a.data_total,axis=0,ignore_index=True,join='outer')
if __name__ == '__main__':
    dd = Download()
    dd.data_concat(URLS,r'result":(\[.*?\])')
    pp=dd.data_total.sort_values(by='sj')
    pp['index']=range(len(pp))
    pp.set_index(['index'])
    pp.to_csv('cpi.csv')



