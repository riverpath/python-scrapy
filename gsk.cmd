@IF EXIST "%~dp0\%1" (
	@echo "��������"
) ELSE (
	@mkdir  "%1" 
	@echo "�ɹ�����%1�ļ���"
)

@IF EXIST "%~dp1" (
	@echo '��������'
	@python run.py "%1"
) ELSE (
	@echo "��ָ������"
)

pause