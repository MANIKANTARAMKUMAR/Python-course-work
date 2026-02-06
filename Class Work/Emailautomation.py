import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'maniknataramkumar760@gmail.com'
password ='mfps ulbq gpen atbu'
receiver_email = 'manikantaramkumar760@gmail.com'
attachment_path = ['productdetails.csv']



def send_email(receiver_email, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        for file in attachment_path:
            attachment = open(file, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
            msg.attach(part)
            attachment.close()
    try:
        server = smtplip.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print(f'Email sent to {receiver_email}')
    except Exception as e:
        print(f'Failed to send email to {receiver_email}. Error: {e}')
def bulk_email(subject, body, attachment_path=None):
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            receiver_email = row[0]
            send_email(receiver_email, subject, body, attachment_path)
send_email('Test Email', 'This is a test email with attachment.', ['productdetails.csv'])