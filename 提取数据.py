import fetchtool.Asyncfetch as myscrapy
import pandas as pd
data=pd.read_excel(u'baidu.xls','baidu')
urls=["https://www.baidu.com/s?wd=" + str(i) + "%40v" for i in data[u'企业名称']]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'百度数据.csv'
myscrapy.fetch_text(urls,pstr,filename)
