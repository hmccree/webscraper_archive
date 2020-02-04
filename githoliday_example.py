import requests
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

#pip install beautifulsoup4
#pip install twilio

url = 'https://hmccree.github.io/HolidayProject2018/'
account_sid = 'AC8e75c8bec3e61cd005fac4f8fec51799'
auth_token = '3972b2a95d919b9623191eecf9f7d6a1'
twilio_phone_number = '+19713510871'
my_phone_number = '+19713446403'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')

free_food = [s for s in soup.body.stripped_strings if 'look for this text' in s.lower()]

if free_food:
    body = 'Free Postmates!\n\n' + '\n'.join(free_food)
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=body,
        to=my_phone_number,
        from_=twilio_phone_number
    )