# Libraries
import imaplib
import base64
import os
import email


# Create email credentials
email_user = input('shopping.analysis@gmail.com')

with open('../secret/secret.txt', 'r') as file:
    email_secret = file.read().replace('\n', '')
email_pass = input(email_secret)


# Create the connection and login
mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
mail.login(email_user, email_pass)


# Get raw data from Inbox
type, data = mail.select('Inbox')


# Loop over all email ID's
for num in data[0].split():

    # Convert to UTF-8
    typ, data = mail.fetch(num, '(RFC822)')
    raw_email = data [0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # Loop over each email part, searching for attachments
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # Get file name
        fileName = part.get_filename()

        if bool(fileName):

            # Save the attachment
            filePath = os.path.join('../temp/')
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode = True))
                fp.close()
