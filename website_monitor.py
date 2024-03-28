import smtplib
import requests
from bs4 import BeautifulSoup
import time
import io 
import os

def send_email(subject, message):
    # Email settings
    sender = os.environ.get('EMAIL_USER')
    receiver = os.environ.get('EMAIL_RECEIVER')
    password = os.environ.get('EMAIL_PASSWORD')
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Email content
    msg = "Subject: {}\n\n{}".format(subject, message)

    # Sending the email
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
    server.quit()

def monitor_website(url, element_class, saved_content_file):
    with io.open(saved_content_file, 'r', encoding='utf-8') as file:
        initial_content = file.read().strip()

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find(class_=element_class)

    if element:
        current_content = element.text.strip()
        if current_content != initial_content:
            print("Change detected! Sending email.")
            send_email("Website Change Detected", "The content of the element with class '{}' has changed.".format(element_class))
            # Update initial_content for subsequent checks
            with io.open(saved_content_file, 'w', encoding='utf-8') as file:
                file.write(current_content)
        else:
            print("No change.")
    else:
        print("Element with class '{}' not found.".format(element_class))

# Example usage
monitor_website("http://ft.org.ua/ua/performance/konotopska-vidma", "performanceevents", "default_content.txt")
