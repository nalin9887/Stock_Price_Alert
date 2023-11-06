STOCK = "IBM" #Enter Name of the company which stock details you want to get

import os
from twilio.rest import Client
import requests
import datetime

current_date = datetime.date.today()
two_days_ago = str(current_date - datetime.timedelta(days=3))
three_days_ago = str(current_date - datetime.timedelta(days=4))
news_api_key=os.environ["news_api_key"]
print(news_api_key)
Stock_Parameter_Apikey=os.environ["Stock_Parameter_Apikey"]
print(Stock_Parameter_Apikey)
Stock_Parameter={"function":"TIME_SERIES_DAILY",
                 "symbol":STOCK,
                 "apikey":os.environ["Stock_Parameter_Apikey"]}            #write your api key
news_parameter={"q":STOCK,
                "from":two_days_ago,
                "sortBy":"publishedAt",
                "apiKey":os.environ["news_api_key"]}                        #write your api key
news_response=requests.get(url="https://newsapi.org/v2/everything", params=news_parameter )


Stock_response=requests.get(url="https://www.alphavantage.co/query", params=Stock_Parameter)
Stock_response.raise_for_status()
data1=float(Stock_response.json()["Time Series (Daily)"][two_days_ago]["4. close"])
data2=float(Stock_response.json()["Time Series (Daily)"][three_days_ago]["1. open"])

change=(data1-data2)/data1*100


if change<-5 or change>5:
    news0_title=news_response.json()["articles"][0]["title"]
    news0_description=news_response.json()["articles"][0]["description"]

    news1_title=news_response.json()["articles"][1]["title"]
    news1_description=news_response.json()["articles"][1]["description"]

    news2_title=news_response.json()["articles"][2]["title"]
    news2_description=news_response.json()["articles"][2]["description"]
    if change<-1:
        symbol="📉"
    else:
     symbol="💹"
    msg=f'''{STOCK} {round(change,3)}% {symbol}

Headline: {news0_title}

Brief: {news0_description}
'''
    print(msg)


    account_sid = 'AC432f71b34a0a62d27eba4f10eded9a99'
    auth_token = '77c093ba04b58e74d6de0eb9e05b0fdd'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='+13345106299',
      body=msg,
      to='+91xxxxxxxxxxx'    #your phone number
    )

    print(message.sid)

    account_sid = 'AC432f71b34a0a62d27eba4f10eded9a99'
    auth_token = '77c093ba04b58e74d6de0eb9e05b0fdd'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=msg,
    to='whatsapp:+91xxxxxxxx'       #your phone number
    )

    print(message.sid)
