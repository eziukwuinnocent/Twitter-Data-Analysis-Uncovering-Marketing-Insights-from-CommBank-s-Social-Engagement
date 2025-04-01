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