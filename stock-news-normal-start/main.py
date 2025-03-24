import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "1ZYVF7EA13X95M3K"
NEWS_API_KEY="8534adfc00f6460eb08461c29523c4e4"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}

response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
#print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
#print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
up_down=None
if difference>0:
    up_down="🔺"
else:
    up_down="🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent=round((difference/float(yesterday_closing_price))*100)
#print(diff_percent)

#If TODO4 percentage is greater than 1 then print("Get News").
if abs(diff_percent)>1:
    news_params={
        "apikey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }

    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]



#use the News API to get articles related to the COMPANY_NAME.


#Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles=[f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    #print(formatted_articles)

    for article in formatted_articles:
        print(article)
        print()
