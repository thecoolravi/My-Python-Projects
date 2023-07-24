# RULES :- Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application


# coding --------------------------------------------

import requests
import json

query = input('News Category? ') 
year = int(input('Year: ')) 
month = int(input('month: '))
date = int(input('date: '))
url = f'https://newsapi.org/v2/everything?q={query}&from={year}-{month}-{date}&sortBy=publishedAt&apiKey=d228cfc45b9d4b6687c5f30824d37dd8'  # news api's url (received it from offial website of news api > logging into website and getting the unique apikey)
r = requests.get(url) #get request on url or all the news from te url

# loads function form json module converts the texts in the r.text to the json format or dictionary format
news = json.loads(r.text) # r.text will convert to text and ten stored in dictonary format because json converts into dictionary


# Now categorizing the articles

# news['articles'] means accessing the key value articles in the dictionary named news
# json.loads sotres in dictonary format thats why news has dictionary content
for article in news['articles']: 
    print('Title: ',article['title']) #prints the title only 
    print('Description: ',article['description']) # prints the description only 
    print('----------------------------------------------')

