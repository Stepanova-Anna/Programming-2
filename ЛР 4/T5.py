import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Настройки
smtp_server = 'smtp.mail.ru'
port = 587
login = 'slouchdogg@mail.ru'
password = 'CQCxTjwjZn9nKZTaG6Dt'
recipient_email = 'stepanna2005@gmail.com'

# Сообщение
message = MIMEMultipart()
message['From'] = login
message['To'] = recipient_email
message['Subject'] = 'Тестовое сообщение'

body = ('Это тестовое сообщение из Python!')
message.attach(MIMEText(body, 'plain'))

# Отправка почты
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.send_message(message)
        print('Почта отправлена!')
except Exception as e:
    print(f'Ошибка: {e}')
