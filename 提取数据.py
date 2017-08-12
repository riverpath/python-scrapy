import fetchtool.Asyncfetch as myscrapy
import pandas as pd
data=pd.read_excel(u'zip.xls',0)
urls=["https://www.qichacha.com/search?key=" + str(i) for i in data[u'企业名称']]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'qicha.xls'
myscrapy.fetch_text(urls,pstr,filename)
