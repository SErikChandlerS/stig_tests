import os
import zipfile
import argparse
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender_email = "stiggggggggggg@gmail.com"
sender_password = "111qaw333"
receiver_email = "nechesanov2000@mail.ru"
subject = "Email с вложением"
body = "Привет, вот архив для тебя!"


def send_email(sender_email, sender_password, receiver_email, subject, body, file_path):
    # Создание объекта сообщения
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Добавление текстового содержимого сообщения
    message.attach(MIMEText(body, "plain"))

    # Открытие и добавление архива в виде вложения
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(file_path)}",
    )

    message.attach(part)

    # Отправка сообщения через SMTP-сервер Gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

        
def create_zip_archive(name):
    files = []
    
    # Поиск файлов с заданным именем
    for file in os.listdir('./tests_collection_2'):
        print(file)
        if name in file:
            files.append(file)
    
    if len(files) == 0:
        print(f"Файлы с названием {name} не найдены.")
        return
    
    # Создание ZIP-архива
    with zipfile.ZipFile(f"{name}_archive.zip", 'w') as zipf:
        for file in files:
            zipf.write('./tests_collection_2/'+file)
    
    print(f"Архив '{name}_archive.zip' успешно создан.")
    zipf.close()
    return '{name}_archive.zip'

# Парсинг аргумента командной строки 'name'
parser = argparse.ArgumentParser(description='Создание ZIP-архива для файлов с заданным именем.')
parser.add_argument('name', type=str)

args = parser.parse_args()

# Вызов функции создания архива с переданным именем
file = create_zip_archive(args.name)

send_email(sender_email, sender_password, receiver_email, subject, body, file)

