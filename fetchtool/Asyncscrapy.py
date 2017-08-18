#coding=utf-8
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient, HTTPError
from tornado.httpclient import HTTPRequest
import requests,re,json,time
from lxml import etree
from . import gooseeker
import hashlib,pdb

class MyClass(object):

    def __init__(self):
        #AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        self.http = AsyncHTTPClient()
        self.headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
   'Accept-Language': 'zh-CN,zh;q=0.8',
   'Accept-Encoding': 'gzip, deflate'}
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
    def set_dis(self,dis):
        self.dis=dis

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
            with open( self.dis +'/' + md5 + '.xml','wb+') as f:
                f.write(result)
            # with open( self.dis +'/' + md5 + '.html','wb+') as f:
            #     f.write(response.body)  
        except:
            print("error")
            # pass
        
class Download(object):

    def __init__(self):
        self.a = MyClass()
    def set_url(self,urls):
        self.urls = urls
    def make_cookie(self,cookie):
        with open(cookie,'r') as f:
            self.a.set_header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
   'Accept-Language': 'zh-CN,zh;q=0.8','Accept-Encoding': 'gzip, deflate',"Cookie":f.read()}

    @coroutine
    def d(self):
        print(r'基于tornado的并发抓取')        
        t1 = time.time()
        yield [self.a.get(url) for url in self.urls]
        t = time.time() - t1
        print(t)

    def data_concat(self,urls,xlst,code,cookie,dis):
        self.set_url(urls)
        self.a.set_xlst(xlst)
        self.a.set_code(code)
        self.a.set_dis(dis)
        self.make_cookie(cookie)
        loop = IOLoop.current()
        loop.run_sync(self.d)

if __name__=="__main__":
    print('success')
