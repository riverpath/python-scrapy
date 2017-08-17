from . import Asyncscrapy
import pandas as pd
from urllib import request
from urllib.parse import quote
import re,json,time
def fetch_text(urls,xlst,code,cookie,dis):
    dd = Asyncscrapy.Download()
    dd.data_concat(urls,xlst,code,cookie,dis)

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
        self.urls=df['URL']

    def setconfig(self,config):
        with open( "./爬虫配置/" + config + "/" + config + ".json",'r',encoding='UTF-8') as f:
            cnf=json.loads(f.read())
        self.arg=cnf['arg']    
        self.cookie=cnf['cookie']
        self.web_code=cnf['code']
        APIKey='9537dede351b975fa8e9dc67f57ea519'
        theme=cnf['theme']
        apiurl = "http://www.gooseeker.com/api/getextractor?key="+ APIKey +"&theme=" + quote(theme)
        self.xlst=request.urlopen(apiurl).read()

    def run(self,arg):
        switch={0:lambda x:self.seturlFromFile(x),1:lambda x:self.seturlFromMem(x)}
        switch['://' in arg](arg)

if __name__ == '__main__':
    urls=["http://content.aetoscg.com/api/getEcoDataList.php?onDate=" + str(i) for i in range(20170101,20170130)]
    pstr=r'data"\:(\[.*?\])'
    filename='cpi.csv'
    fetch_text(urls,pstr,filename)
