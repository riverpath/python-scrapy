#coding=utf-8
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient, HTTPError
from tornado.httpclient import HTTPRequest
import requests,re,json,time
import pandas as pd
import numpy as np



URLS = ["http://data.stats.gov.cn/search.htm?s=CPI&m=searchdata&db=&p=" + str(i) for i in range(201)]

class MyClass(object):

    def __init__(self):
        #AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        self.http = AsyncHTTPClient()
        self.data_total=[]
        self.headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
   'Accept-Language': 'zh-CN,zh;q=0.8',
   'Accept-Encoding': 'gzip, deflate',}
    @coroutine  
    def get(self, url,pstr):
        #tornado会自动在请求首部带上host首部        
        request = HTTPRequest(url=url,
                            method='GET',
                            headers=self.headers,
                            connect_timeout=20.0,
                            request_timeout=60.0,
                            follow_redirects=False,
                            max_redirects=False,
                            user_agent="Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36",)
        yield self.http.fetch(request, callback=self.find(response,pstr=pstr), raise_error=False)
    def set_pstr(self,pstr):
        self.pstr=pstr
    def set_header(self,headers):
        self.headers=headers
    def find(self, response,pstr):
        if response.error:
            print(response.error)
        print(response.code, response.effective_url, response.request_time )
        try:
            pat=re.compile(pstr,re.S)
            m=pat.search(response.body.decode('utf-8')) 
            self.data_total.append(pd.DataFrame(json.loads(m.group(1))))
        except:
            print("error")
        
class Download(object):

    def __init__(self):
        self.a = MyClass()
    def set_url(self,urls):
        self.urls = urls
    def set_pstrs(self,pstrs):
        self.pstrs =pstrs
    @coroutine
    def d(self):
        print(r'基于tornado的并发抓取')        
        t1 = time.time()
        yield [self.a.get(url,pstr) for url,pstr in zip(self.urls,self.pstrs)]
        t = time.time() - t1
        print(t)

    def data_concat(self,urls,pstr):
        self.set_url(urls)
        self.set_pstrs(pstr)
        loop = IOLoop.current()
        loop.run_sync(self.d)
        self.data_total=pd.concat(self.a.data_total,axis=0,ignore_index=True,join='outer')
if __name__ == '__main__':
    dd = Download()
    dd.data_concat(URLS,r'result":(\[.*?\])')
    dd.data_total.to_csv('cpi.csv')

