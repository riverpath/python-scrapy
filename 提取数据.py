import fetchtool.Asyncfetch as myscrapy
import pandas as pd
data=pd.read_excel(u'zip.xlsx',0)
urls=data['URL']
filename=u'Alibaba.csv'
pstr="a"
myscrapy.fetch_text(urls,pstr,filename)
