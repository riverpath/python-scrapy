@IF EXIST "%~dp0\data" (
 @echo '��������'
) ELSE (
  @mkdir  "%~dp0\data" 
@echo '�����ɹ�����������'
)

@set var1="�۴���ϵ"
@set var2="il.xlsx"

@python ��ȡ����.py %var1% %var2%
@rename data %var1%
pause