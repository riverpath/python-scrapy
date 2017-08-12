import fetchtool.Asyncfetch as myscrapy
import pandas as pd
data=pd.read_excel(u'zip.xls',0)
urls=["https://www.baidu.com/s?wd=" + str(i) + "%40v" for i in data[u'企业名称']]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'baidu.xls'
myscrapy.fetch_text(urls,pstr,filename)
