import base64
import codecs
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

CLIENT_FILE = 'token.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
#SCOPES = ['https://mail.google.com/']
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
f = codecs.open('message.txt', 'r', 'utf-8')
emailMsg = f.read()
f.close()

creds = Credentials.from_authorized_user_file(CLIENT_FILE, SCOPES)
service = build(API_NAME, API_VERSION, credentials=creds)
mimeMessage = MIMEMultipart()
mimeMessage['subject'] = 'בדיקה'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
with open("Mails.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for email in reader:
        mimeMessage['to'] = email[1]
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        