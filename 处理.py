import pandas as pd
df2=pd.read_excel(u'zip.xls',0)
df1=pd.read_excel(u'qicha.xls',0)
result = pd.merge(df1,df2,on=u"企业名称",how="left")
result.to_excel(u'data.xls','sh')