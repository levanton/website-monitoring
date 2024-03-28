# -*- coding: utf-8 -*-

import smtplib

def send_email(subject, message):
    # Email settings
    sender = "levanton21@gmail.com"
    receiver = "levanton21@gmail.com"
    password = "fbav iwdr pfzp qipq"
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Ensure subject and message are unicode
    if not isinstance(subject, unicode):
        subject = unicode(subject, 'utf-8')
    if not isinstance(message, unicode):
        message = unicode(message, 'utf-8')

    # Email content
    msg = u"Subject: {}\n\n{}".format(subject, message).encode('utf-8')

    # Sending the email
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
    server.quit()

# Sending the email
send_email("Привет", "Привет, как дела?")
