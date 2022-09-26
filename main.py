from twilio.rest import Client
import requests
from datetime import date
from datetime import timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
newsapi='f64708643fdc4b4194df57bfa7ec04b2'
account_sid='AC770dce05b1b4824a4b8afc69b3e1934a'
auth_token='402acd15438d602520a33eec2516e982'

datet=date.today()
dateyesterday=datet-timedelta(days=1)
datedaybefore=datet-timedelta(days=2)


parameters={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':'ZIEYATXWWI5VTYPR'
}
response=requests.get(url='https://www.alphavantage.co/query',params=parameters)
data=response.json()
yesterday=float(data["Time Series (Daily)"][f'{dateyesterday}']['4. close'])
daybefore=float(data["Time Series (Daily)"][f'{datedaybefore}']['4. close'])


diff=(yesterday-daybefore)
updown=None
if diff>0:
    updown='⬆️'
else:
    updown='⬇️'

percentagev=round((diff/yesterday)*100)



if abs(percentagev)>1:


    parameters1={'q':COMPANY_NAME,
                'from':f'{dateyesterday}',
                'sortBy':'popularity',
                'apiKey':newsapi,

    }

    response1=requests.get(url='https://newsapi.org/v2/everything',params=parameters1)
    data1=response1.json()['articles']
    threearticles=data1[:3]




    formattedarticle=[f"{STOCK}: {updown} {percentagev}%\nHeadlines: {articles['title']}.\n Brief: {articles['description']}" for articles in threearticles]

    for articles1 in formattedarticle:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=articles1,
            from_='+1 985 531 1090',
            to='+91 98409 13995'
        )
        print(message.status)


