import requests
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time
from variables import *
import html2text


url = input("url of website: ")
# this whole part is unnecessary - invalid links will abort program w/o harm
# link_test = requests.get(url)
# link_test_code = link_test.status_code
# if(link_test_code == 200):
#     print('link is valid')

# requests.get has a built-in link checker - process aborts if link isn't valid
# else:
    # url = 'https://hmccree.github.io/HolidayProject2018/'
    # print('link not valid, defaulting to https://hmccree.github.io/HolidayProject2018/')
client = Client(account_sid, auth_token)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
newtext = str(soup)
web_text = html2text.html2text(newtext)
# print(text)
# soup_pretty = soup.prettify()
# soup_p_tag = soup.find_all('p')[0].get_text()
print("text from page: \n" + str(web_text))
op_type = input("look for word [w] or changes [c]?: ")
#get input for the word to find, checking times, and cancellation
# global count_checks
# count_checks = 0


time_between_checks = int(input("time between checks (seconds): "))
if(time_between_checks < 10):
    print("value too low, defaulting to 15 seconds")
    time_between_checks = 15


#send messages if the input word is found in the pave text
def look_for_word():
    count_checks = 0
    word_to_find = input("word to find: ")
    amount_of_checks = int(input("times to check for word: "))
    cancel_after_success = input("cancel process after a successful check? [Y/N]: ")
    if(cancel_after_success == 'Y' or cancel_after_success == 'y'):
        cancel_after_success = True
    elif(cancel_after_success == 'N' or cancel_after_success == 'n'):
        cancel_after_success = False
    else:
        print("input not recognized")
    while True:
        count_checks += 1
        print("Checks: " + str(count_checks))
        # check_for_updates()
        if(word_to_find in web_text):
            client.messages.create(body="Word '" + word_to_find + "' found in page",to=my_phone_number,from_=twilio_phone_number)
            if(cancel_after_success):
                print("sent message, process cancelled")
                break
            else:
                print("sent message, process still running")
        if(count_checks >= amount_of_checks):
            break
            # this print statement is somehow out of reach
            # print("process cancelled")
        time.sleep(time_between_checks)
        # if(sent_check > 0):
            # break


def look_for_changes():
    count_checks = 0
    while True:
        count_checks += 1
        print("Checks: " + str(count_checks))
        page_new = requests.get(url)
        soup_new = BeautifulSoup(page_new.content, 'html.parser')
        newtext_new = str(soup_new)
        web_text_new = html2text.html2text(newtext_new)
        if(web_text_new != web_text):
            client.messages.create(body="Page has changed since last check",to=my_phone_number,from_=twilio_phone_number)
            break
        else:
            time.sleep(time_between_checks)
        

if(op_type == 'w' or op_type == 'W'):
    look_for_word()
elif(op_type == 'c' or op_type == 'C'):
    look_for_changes()

# url = otherfile_url
# account_sid = otherfile_account_sid
# auth_token = otherfile_auth_token
# twilio_phone_number = otherfile_twilio_phone_number
# my_phone_number = otherfile_my_phone_number


# check for changes in a page - not for this assignment
# check for sent doesn't work
# sent_check = 0
# def check_for_updates():
#     page_new = requests.get(url)
#     soup_new = BeautifulSoup(page_new.content, 'html.parser')
#     soup_new_pretty = soup_new.prettify()
#     if(soup_new_pretty != soup_pretty):
#         print("Sent message")
#         client.messages.create(body="The page has changed!",to=my_phone_number,from_=twilio_phone_number)
#         # sent_check = 1