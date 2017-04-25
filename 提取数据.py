import fetchtool.Asyncfetch as myscrapy
urls=["http://data.stats.gov.cn/search.htm?s=GDP&m=searchdata&db=&p=" + str(i) for i in range(201)]
pstr=r'result"\:(\[.*?\])'
filename=u'数据/GDP.csv'
myscrapy.fetch_text(urls,pstr,filename)
