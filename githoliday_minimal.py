import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from variables import *
import html2text
import time

url = input("url of website: ")
client = Client(account_sid, auth_token)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
newtext = str(soup)
web_text = html2text.html2text(newtext)
print("text from page: \n" + str(web_text))
count_checks = 0
word_to_find = input("word to search for:")

while True:
    if(word_to_find in web_text):
        client.messages.create(body="Word '" + word_to_find + "' found in page",to=my_phone_number,from_=twilio_phone_number)
        break
    else:
        count_checks += 1
        if(count_checks >= 10):
            break
        else:
            time.sleep(30)
            continue