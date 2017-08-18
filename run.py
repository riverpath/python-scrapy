import fetchtool.Asyncfetch as myscrapy
from sys import argv
import pdb,time
# 从api之中获取模块

file_main,theme=argv
URLS=myscrapy.webclass()
URLS.setconfig(theme)
URLS.run(URLS.argurl)

myscrapy.fetch_text(URLS.urls,URLS.xlst,URLS.web_code,URLS.cookie,theme)

# f=lambda a:map(lambda b:a[b:b+4],range(0,len(a),4))
# arv=f(URLS.urls)
# for i in arv:
#     myscrapy.fetch_text(i,URLS.xlst,URLS.web_code,URLS.cookie,theme)
#     time.sleep(15)