import smtplib
from email.message  import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'sender@outlook.com'
email['to'] = 'recipient@gmail.com'
email['subject'] = 'You\'re filthy rich!!'
email.set_content(html.substitute({'name': 'Ciaran', 'amount': 50000}), 'html')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@outlook.com', 'Password')
    smtp.send_message(email)
print('all good boss!')
