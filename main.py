import requests
from bs4 import BeautifulSoup
import re

URL = 'https://ultimatehackingkeyboard.com/delivery-status'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
post_content = soup.find('div', class_='post-content')
if post_content:
    text_list = post_content.find_all('p')

    text=""
    for phrase in text_list:
        text+=phrase.text

    try:
        first_order_to_be_shipped = re.search('to be shipped next is #(.+?),', text).group(1)
    except AttributeError:
        first_order_to_be_shipped = ''

    try:
        last_order = re.search(' the last order is #(.+?),', text).group(1)
    except AttributeError:
        last_order = ''


    try:
        updated_date = re.search('page was updated on (.+?)\.', text).group(1)
    except AttributeError:
        updated_date = ''

    print(" | ".join([updated_date, first_order_to_be_shipped, last_order]))
    # print("first_order_to_be_shipped", first_order_to_be_shipped)
    # print("last_order", last_order)
    # print("updated_date", updated_date)
