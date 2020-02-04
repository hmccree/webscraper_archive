from bs4 import BeautifulSoup #for html parsing
import requests #for getting the site
from twilio.rest import Client #for sending the message
import time #for delays
# from variables import * #import your variables from variables.py
import html2text

url = 'https://hmccree.github.io/HolidayProject2018/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text = str(soup)
web_text = html2text.html2text(text)
print(web_text)

time.sleep(60)

page_new = requests.get(url)
soup_new = BeautifulSoup(page_new.content, 'html.parser')
text_new = str(soup_new)
web_text_new = html2text.html2text(text_new)
print(web_text_new)

print('equal:')
print(web_text == web_text_new)