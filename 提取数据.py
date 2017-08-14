import fetchtool.Asyncfetch as myscrapy
import pandas as pd
# data=pd.read_excel(u'zip.xls',0)
urls=["http://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2587%2591%25E8%259E%258D,2," + str(i) + ".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=" for i in range(1,2001)]
pstr=r'span class\="cust\-num"\>(.*?)\<'
filename=u'51job.xlsx'
myscrapy.fetch_text(urls,pstr,filename)
