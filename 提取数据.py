import fetchtool.Asyncfetch as myscrapy
import pandas as pd
data=pd.read_excel(u'C:/Users/Administrator/Desktop/2017081014212131616845.xls','tuiguang')
urls=["https://www.baidu.com/s?wd=" + str(i) + "%40v" for i in data[u'企业名称']]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'数据/GDP.csv'
myscrapy.fetch_text(urls,pstr,filename)
