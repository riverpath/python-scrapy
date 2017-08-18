@IF EXIST "%~dp0\鰾單饜离\%1" (
	@echo "葩秶恅璃"
) ELSE (
	@mkdir  ".\鰾單饜离\%1" 
	@echo "傖髡斐膘%1恅璃標")
@copy .\鰾單饜离\default\default.json  .\鰾單饜离\%1\%1.json
@copy .\鰾單饜离\default\default.xlsx  .\鰾單饜离\%1\%1.xlsx
@copy .\鰾單饜离\default\default.txt  .\鰾單饜离\%1\%1.txt
@python project.py %1
pause
