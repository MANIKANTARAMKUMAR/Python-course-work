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
password = 'gtqn wuhf exba psia'
receiver_email = 'manikantaramkumar760@gmail.com'


def send_email(receiver_email, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        for file in attachment_path:
            with open(file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(file)}'
                )
                msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f'Email sent to {receiver_email}')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')


# ✅ correct call
send_email(
    receiver_email,
    'Test Email',
    'This is a test email with attachment.',
    ['productdetails.csv']
)
