import fetchtool.Asyncfetch as myscrapy
import pandas as pd
from urllib import request
from urllib.parse import quote
import re,json
# 从api之中获取模块

arg='http://s.hc360.com/?w=%CA%B3%C6%B7&mc=enterprise&ee=[[1,6,1]]&z=%D6%D0%B9%FA%3A%D5%E3%BD%AD%CA%A1'
theme=u'慧聪公司'

# xlst='xslt_bbs.xml'
# print(apiurl)
# 获取url地址
class webclass(object):
    def __init__(self):
        self.pat=r'(.*?)\[(\[.*?\])\](.*)'
    def seturlFromMem(self,url):
        self.url=url
        pattern=re.compile(self.pat)
        gr=pattern.search(self.url)
        ar=json.loads(gr.group(2))
        self.urls=[gr.group(1) + str(i) + gr.group(3) for i in range(ar[0],ar[1],ar[2]) ]
    def seturlFromFile(self,fileName):
        self.fileName=fileName
        df=pd.read_excel(fileName,0)
        self.urls=df[URL]

APIKey='9537dede351b975fa8e9dc67f57ea519'
apiurl = "http://www.gooseeker.com/api/getextractor?key="+ APIKey +"&theme=" + quote(theme)
xlst=request.urlopen(apiurl).read()
URLS=webclass()
switch={0:lambda x:URLS.seturlFromFile(x),1:lambda x:URLS.seturlFromMem(x)}
switch['http://' in arg](arg)
myscrapy.fetch_text(URLS.urls,xlst,code='gbk')