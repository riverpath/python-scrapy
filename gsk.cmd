@IF EXIST "%~dp0\%1" (
	@echo "程序载入"
) ELSE (
	@mkdir  "%1" 
	@echo "成功创建%1文件夹"
)

@IF EXIST "%~dp1" (
	@echo '正在启动'
	@python 提取数据.py "%1"
) ELSE (
	@echo "请指定配置"
)

pause