import json,os,sys
filename,theme=sys.argv
with open("./爬虫配置/" + theme + "/"+ theme + ".json",'w+',encoding='utf-8') as f:
    f.write('{\n"argurl": "./爬虫配置/%s/%s.xlsx",\n"theme": "http://www.gooseeker.com/api/getextractor?key=9537dede351b975fa8e9dc67f57ea519&theme=true_path%s",\n"code":"utf-8",\n"cookie":"./爬虫配置/%s/%s.txt"\n}' %(theme,theme,theme,theme,theme))