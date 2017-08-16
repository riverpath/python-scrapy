@IF EXIST "%~dp0\data" (
 @echo '正在启动'
) ELSE (
  @mkdir  "%~dp0\data" 
@echo '创建成功，正在启动'
)

@set var1="慧聪联系"
@set var2="il.xlsx"

@python 提取数据.py %var1% %var2%
@rename data %var1%
pause