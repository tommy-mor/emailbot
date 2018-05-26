"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
import schedule
import time
import base64
import argparse

# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

def send_email():
    # Call the Gmail API
    message = MIMEText('do your homework body')
    message['to'] = 'thmorriss@gmail.com'
    message['from'] = 'thmorriss@gmail.com'
    message['subject'] = 'do your homework'

    message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    results = service.users().messages().send(userId='me', body=message).execute()
    print(results)

parser = argparse.ArgumentParser()
parser.add_argument('--schedule', dest='sched', action='store_const', default=False, const=True)
args = parser.parse_args()
print(args.sched)
if (args.sched):
    schedule.every().day.at("13:00").do(send_email)
    while True:
        schedule.run_pending()
    time.sleep(60)
else:
    send_email()
