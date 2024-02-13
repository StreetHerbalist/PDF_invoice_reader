import imaplib
import email
import json
import os

class extractor():
    with open('StreetHerbalist/PDF_invoice_reader/email_reader/credentials.json', 'r') as file:
            credentials= json.load(file)
    email_ = credentials("e-mail")
    password= credentials("password")
    imap_url = "impap.gmail.com"
    def __init__():
        return None
    
    def email_reader(self):
        our_mail = imaplib.IMAP4_SSL(self.imap_url)
        our_mail.login(self.email_, self.password)
        our_mail.select("Inbox")
        result, data = our_mail.search(None, '(BODY "application/pdf")')
        for num in data[0].split():
            result, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            for part in msg.walk():
                if part.get_content_type() == 'application/pdf':
                    filename = part.get_filename()
                    if filename:
                        filepath = os.path.join('pdf_attachments', filename)
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))


instnc = extractor()
instnc.__init__()
instnc.email_reader()