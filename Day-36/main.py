import os
import time
import requests
import json
from itertools import islice
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]
PHONE = os.environ.get("PHONE_NUMBER")
COMPANY_NAME = "Tesla Inc"

STOCK = "TSLA"
ALPHA_VANTAGE_API = os.environ.get('ALPHA_VANTAGE_API')
ALPHA_URL = 'https://www.alphavantage.co/query'

ALPHA_PARAMETERS = {
    'function' : 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol' : STOCK,
    'outputsize' : 'compact',
    'apikey' : ALPHA_VANTAGE_API
}

NEWS_API = os.environ.get('NEWS_API')
NEWS_URL = 'https://newsapi.org/v2/everything'


def percent_diff(a=float, b=float):
    return round((a - b) / a * 100, 2)
    # return -5

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=ALPHA_URL, params=ALPHA_PARAMETERS).json()

last_2_days_stock = list(stock_response['Time Series (Daily)'].items())[:2]
yesterday_open = float(last_2_days_stock[0][1]['1. open'])
before_yesterday_close = float(last_2_days_stock[1][1]['4. close'])
close_day = last_2_days_stock[1][0]
different = percent_diff(yesterday_open, before_yesterday_close)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
NEWS_PARAMETERS = {
    'q' : COMPANY_NAME,
    'apiKey' : NEWS_API,
    'from' : close_day,
    'searchIn' : 'description'
}
if abs(different) >= 5:
    news_response = requests.get(url=NEWS_URL, params=NEWS_PARAMETERS).json()
    news_data = news_response['articles'][:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
for message in news_data:
    msg = f'TSLA: {"🔺" if different > 0 else "🔻"}{abs(different)}\n\
        Headline: {message["title"]}\n\
        Brief: {message["description"]}\n\
        {message["url"]}'
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    twilio_msg = client.messages.create(
    body=msg,
    from_="+12706388747",
    to=PHONE
    )

