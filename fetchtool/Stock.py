import requests,re,json,sys
from pandas import DataFrame,Series
def getcontent(code):
    url=u'http://api.finance.ifeng.com/akdaily/?code='+ code + u'&type=last'
    res=requests.get(url)
    pat=re.compile(r"(\[\[.*?\]\])",re.S)
    m=pat.search(res.text)
    if m: 
        print('success')
    m
    tt=json.loads(m.group(1))
    columns=[u"日期",u"开盘价",u"最高价",u"收盘价",u"最低价",u"成交量",u"涨跌额",u"涨跌幅",u"5日均价",u"10日均价",u"20日均价",u"5日均量",u"10日均量",u"20日均量",u"换手率"]
    frame=DataFrame(tt,columns=columns)
    frame[[u"开盘价",u"最高价",u"收盘价",u"最低价",u"成交量",u"涨跌额",u"涨跌幅",u"5日均价",u"10日均价",u"20日均价",u"换手率"]]=frame[[u"开盘价",u"最高价",u"收盘价",u"最低价",u"成交量",u"涨跌额",u"涨跌幅",u"5日均价",u"10日均价",u"20日均价",u"换手率"]].astype(float)
    frame[u"5日均量"]=frame[u"5日均量"].str.replace(',','').astype(float)
    frame[u"10日均量"]=frame[u"10日均量"].str.replace(',','').astype(float)
    frame[u"20日均量"]=frame[u"20日均量"].str.replace(',','').astype(float)
    frame.set_index([u'日期']).to_csv(code +'.csv')
if __name__=="__main__":
    print(sys.argv[1])
    for a in sys.argv[1].split(','):
        getcontent(a)
