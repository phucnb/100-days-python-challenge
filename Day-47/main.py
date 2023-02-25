from bs4 import BeautifulSoup
import requests, os
import lxml
from itertools import islice
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]
PHONE = os.environ.get("PHONE_NUMBER")


URL = 'https://a.co/d/7zdJMCi'
TARGET_PRICE = 25

header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
    'Accept-Language' : 'en-CA,en-US;q=0.9,en;q=0.8'
    }
    
html = requests.get(url=URL, headers=header)
soup = BeautifulSoup(html.text, 'lxml')

def get_current_price(soup):
    whole_price = soup.find('span', class_='a-price-whole').getText().strip()
    fraction_price = soup.find('span', class_='a-price-fraction').getText().strip()
    return float(whole_price+fraction_price)

def get_product_name(soup):
    return soup.find('title').getText().split(' – ')[0]


if get_current_price(soup) < TARGET_PRICE:
    # TODO: Send SMS
    msg = f"{get_product_name(soup=soup)}'s price dropped to {get_current_price(soup)}\n Go to {URL} to buy"
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    twilio_msg = client.messages.create(
    body=msg,
    from_="+12706388747",
    to=PHONE
    )

