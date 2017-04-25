import urllib.request,re,json
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
def fetch(a):
    try:
            response=urllib.request.urlopen(a[0])
    except:
        response=None
    if response!=None:
        print(response.code, response.url,a[1])
        pat=re.compile(a[1],re.S)
        m=pat.search(response.read().decode('utf-8')) 
        
        return pd.DataFrame(json.loads(m.group(1)))
    else:
        print('error')

urls=[('http://data.stats.gov.cn/search.htm?s=CPI&m=searchdata&db=&p=' + str(i),r'result\"\:(\[.*?\])' ) for i in range(10)]
pool=ThreadPool(4)
results=pool.map(fetch,urls)
pool.close()
pool.join