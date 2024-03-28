# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import io

def save_current_version(url, element_class, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find(class_=element_class)

    if element:
        current_content = element.text.strip()
        with io.open(output_file, 'w', encoding='utf-8') as file:  # Use io.open for encoding
            file.write(current_content)
        print("Current version saved.")
    else:
        print("Element with class '{}' not found.".format(element_class))

# Пример использования
save_current_version("http://ft.org.ua/ua/performance/konotopska-vidma", "performanceevents", "default_content.txt")
