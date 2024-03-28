import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_email(subject, message):
    # Email settings
    sender = "your_email@example.com"
    receiver = "receiver_email@example.com"
    password = "your_password"
    smtp_server = "smtp.example.com"
    port = 587  # For starttls

    # Email content
    msg = f"Subject: {subject}\n\n{message}"

    # Sending the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg)
        server.quit()

def check_website():
    url = "https://example.com"
    element_selector = "div.some-class"  # Change this to the CSS selector of the element you want to monitor

    # Fetching the website content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.select_one(element_selector)

    if element:
        current_content = element.text.strip()
        if current_content != previous_content[0]:
            previous_content[0] = current_content
            send_email("Website Change Detected", f"The content has changed: {current_content}")
    else:
        print("Element not found")

if __name__ == "__main__":
    previous_content = [""]
    while True:
        check_website()
        time.sleep(300)  # Check every 5 minutes