import fetchtool.Asyncfetch as myscrapy
import pandas as pd
from urllib import request
from urllib.parse import quote
# 从api之中获取模块
theme='job51'
APIKey='9537dede351b975fa8e9dc67f57ea519'
apiurl = "http://www.gooseeker.com/api/getextractor?key="+ APIKey +"&theme=" + quote(theme)
xlst=request.urlopen(apiurl).read()
# xlst='xslt_bbs.xml'

# 获取url地址
urls=["http://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2587%2591%25E8%259E%258D,2," + str(i) + ".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=" for i in range(1,100)]

myscrapy.fetch_text(urls,xlst,code='gbk')