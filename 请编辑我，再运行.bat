@IF EXIST "%~dp0\data" (
 @echo '��������'
) ELSE (
  @mkdir  "%~dp0\data" 
@echo '�����ɹ�����������'
)

@python ��ȡ����.py 

pause