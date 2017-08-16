@IF EXIST "%~dp0\data" (
 @echo '正在启动'
) ELSE (
  @mkdir  "%~dp0\data" 
@echo '创建成功，正在启动'
)

@python 提取数据.py 

pause