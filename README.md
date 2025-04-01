# Twitter Data Analysis: Uncovering Marketing Insights from CommBank's Social Engagement

![Image Alt](https://github.com/eziukwuinnocent/Twitter-Data-Analysis-Uncovering-Marketing-Insights-from-CommBank-s-Social-Engagement/blob/9104d9472c2aa34d9280b83e987b219b24d1440b/CommBank.jpg)

This project aimed to provide CommBank with data-driven marketing intelligence by analyzing their Twitter presence. I employed Python and web scraping techniques to gather data on CommBank's tweets, user interactions, and audience demographics. 

The project mainly focused on transforming unstructured Twitter (X) data into structured data for potential marketing intelligence regarding CommBank. Utilizing Python for web scraping, I successfully extracted and structured data from CommBank's Twitter activity, creating a comprehensive table. This structured data is now prepared for further analysis, including examining tweet engagement metrics, performing sentiment analysis on replies and quote retweets, analyzing user mentions, and profiling audience demographics. This structured dataset lays the groundwork for a data-driven understanding of CommBank's audience, enabling targeted marketing strategies in future analysis.

### 
import pandas as pd

import numpy as np

from bs4 import BeautifulSoup

import requests


reviews  = []
stars = []
date = []
country = []

for i in range(1, 36):
    page = requests.get(f"https://www.airlinequality.com/airline-reviews/british-airways/page/{i}/?sortby=post_date%3ADesc&pagesize=100")
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    for item in soup.find_all("div", class_="text_content"):
        reviews.append(item.text)
    
    for item in soup.find_all("div", class_ = "rating-10"):
        try:
            stars.append(item.span.text)
        except:
            print(f"Error on page {i}")
            stars.append("None")
            
    #date
    for item in soup.find_all("time"):
        date.append(item.text)
        
    #country
    for item in soup.find_all("h3"):
        country.append(item.span.next_sibling.text.strip(" ()"))
        
        
len(reviews)
len(stars)
len(date)
len(country)

stars = stars[:3500]
print(stars)

reviews_series = pd.Series(reviews)

stars_series = pd.Series(stars)

date_series = pd.Series(date)

country_series = pd.Series(country)

df = pd.DataFrame({"reviews": reviews_series, "stars": stars_series, "date": date_series, "country": country_series})

print(df)

BA_table = df.to_csv("BA.csv", index= True)

BA_table
