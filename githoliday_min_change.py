from bs4 import BeautifulSoup #for html parsing
import requests #for getting the site
from twilio.rest import Client #for sending the message
import time #for delays
from variables import * #import your variables from variables.py
import html2text

count = 0
url = 'https://hmccree.github.io/HolidayProject2018/'
interval = int(input('interval [seconds]: '))
if(interval <= 10):
    print('too low, defaulting to 15')
    interval = 15

def send_message():
    client = Client(account_sid, auth_token)
    client.messages.create(body='Page has changed',to=my_phone_number,from_=twilio_phone_number)

while True:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = str(soup)
    web_text = html2text.html2text(text)
    # print(web_text)

    time.sleep(interval)

    page_new = requests.get(url)
    soup_new = BeautifulSoup(page_new.content, 'html.parser')
    text_new = str(soup_new)
    web_text_new = html2text.html2text(text_new)
    # print(web_text_new)
    count += 1

    print('check ' + str(count))
    print(web_text == web_text_new)

    #never finds a change
    if(web_text != web_text_new):
        print('changed')
        send_message()
        continue
    elif(web_text == web_text_new):
        print('no change')
        continue
    else:
        print('something has gone wrong')
        break