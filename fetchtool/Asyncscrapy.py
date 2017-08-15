#coding=utf-8
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient, HTTPError
from tornado.httpclient import HTTPRequest
import requests,re,json,time
from lxml import etree
from . import gooseeker
import hashlib
with open('cookie.txt','r') as f:
    cookie_data=f.read()
class MyClass(object):

    def __init__(self):
        #AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        self.http = AsyncHTTPClient()
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
    def set_header(self,headers):
        self.headers=headers
    def set_xlst(self,xlst):
        self.xlst=xlst
    def set_code(self,code):
        self.code=code
    def find(self, response):
        if response.error:
            # print(response.error)
            pass
        # print(response.code, response.effective_url, response.request_time )
        # print(self.xlst)
        try:
            doc=etree.HTML(response.body.decode(self.code,'ignore'))
            bbsExtra = gooseeker.GsExtractor() 
            bbsExtra.setXsltFromMem(self.xlst)
            result = bbsExtra.extract(doc) # 调用extract方法提取所需内容
            md5=hashlib.md5(response.effective_url.encode('utf-8')).hexdigest()
            with open( 'data/' + md5 + '.xml','wb') as f:
                f.write(result)
        except:
            print("error")
            # pass
        
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

    def data_concat(self,urls,xlst,code):
        self.set_url(urls)
        self.a.set_xlst(xlst)
        self.a.set_code(code)
        loop = IOLoop.current()
        loop.run_sync(self.d)


