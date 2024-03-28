import requests
from bs4 import BeautifulSoup
import smtplib
import time
from unidecode import unidecode

def send_email(subject, message):
    # Email settings
    sender = "smtp.gmail.com"
    receiver = "levanton21@gmail.com"
    password = "${{ secrets.GMAIL_PASSWORD }}"
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Email content
    msg = "Subject: {}\n\n{}".format(subject, message)

    # Sending the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, unidecode(msg))
        server.quit()

def check_website():
    url = "http://ft.org.ua/ua/performance/konotopska-vidma"
    element_selector = "div.performanceevents"  # Change this to the CSS selector of the element you want to monitor

    # Fetching the website content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.select_one(element_selector)

    if element:
        current_content = element.text.strip()
        if current_content != previous_content[0]:
            previous_content[0] = current_content
            send_email("Website Change Detected", "The content has changed: {}".format(current_content))
    else:
        print("Element not found")

if __name__ == "__main__":
    previous_content = [""]
    while True:
        check_website()
        time.sleep(300)  # Check every 5 minutes
