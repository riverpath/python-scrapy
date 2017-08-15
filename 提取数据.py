import fetchtool.Asyncfetch as myscrapy
import pandas as pd
# data=pd.read_excel(u'zip.xls',0)
urls=["https://s.1688.com/selloffer/offer_search.htm?spm=a2604.8117111.iq3gamj1.7.CR0Wba&uniqfield=pic_tag_id&keywords=%C5%A3%D7%D0%BF%E3+%C5%AE&earseDirect=false&filtHolidayTagId=10010608&n=y&filt=y#beginPage=" + str(i) for i in range(1,7)]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'Alibaba.csv'
myscrapy.fetch_text(urls,pstr,filename)
