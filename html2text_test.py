import requests
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time
# from variables import *
import html2text


url = 'https://hmccree.github.io/HolidayProject2018/'
# client = Client(account_sid, auth_token)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
newtext = str(soup)

text = html2text.html2text(newtext)
print(text)