@echo OFF
if not exist token.json (
	echo please choose your gmail account and select continue twice
	pause
	)
python.exe createToken.py
echo Press enter to send mails
pause >nul
echo sending mails
python.exe MailSender.py
echo Mails sent, press any key to close
pause >nul