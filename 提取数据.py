import fetchtool.Asyncfetch as myscrapy
import pandas as pd
# data=pd.read_excel(u'zip.xls',0)
urls=["https://www.itjuzi.com/company/" + str(i) for i in range(80915,80918)]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'It桔子.csv'
myscrapy.fetch_text(urls,pstr,filename)
