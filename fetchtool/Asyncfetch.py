from . import Asyncscrapy
def fetch_text(urls,pstr,filename):
    dd = Asyncscrapy.Download()
    dd.data_concat(urls,pstr)
    dd.data_total.to_excel(filename,'datascrapy')

if __name__ == '__main__':
    urls=["http://content.aetoscg.com/api/getEcoDataList.php?onDate=" + str(i) for i in range(20170101,20170130)]
    pstr=r'data"\:(\[.*?\])'
    filename='cpi.csv'
    fetch_text(urls,pstr,filename)
