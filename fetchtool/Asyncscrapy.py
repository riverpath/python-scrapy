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
        # print(response.code, response.effective_url, response.request_time )
        try:
            tree=etree.HTML(response.body.decode('utf-8','ignore'))
            a=tree.xpath('//*[@id="searchlist"]//em/text()')[0].strip()
            b=tree.xpath('//*[@id="searchlist"]/table//a/text()')[0].strip()
            c=tree.xpath('//*[@id="searchlist"]//span/text()')[1].strip().split('：')[1]
            d=tree.xpath('//*[@id="searchlist"]//span/text()')[0].strip().split('：')[1]
            e=''.join(tree.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[3]/text()')).strip().split('：')[1]
            f=tree.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[2]/span/text()')[0].strip().split('：')[1]
            g=tree.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[2]/text()')[0].strip().split('：')[1]
            h=response.effective_url
            if tree!=None:
                self.data_total.append(pd.DataFrame({'企业名称':[a],'法人代表':[b],'成立日期':[c],'注册资本':[d],'地址':[e],'邮箱':[f],'电话号码':[g],'网址':[h]}))
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



