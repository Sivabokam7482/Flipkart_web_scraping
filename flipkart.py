import requests
from bs4 import BeautifulSoup
import json,csv,time
import pandas as pd 

import os
os.system('cls')

print(f"{"*"*27} WELCOME TO FLIPKART WEB SCRAPING {"*"*27}")
print()
Names=[]
Prices=[]
Ratings=[]
Reviews=[]

Num_pages= int(input("How many pages to scraped data Do you want? : "))
for page in range(1,Num_pages+1):
    url = f"https://www.flipkart.com/search?q=laptops&page={page}"
    # Send request and get HTML content   
    r=requests.get(url)
    # Parse HTML content
    soup=BeautifulSoup(r.content,"html.parser")
    p_names=soup.find_all('div',class_="KzDlHZ")
    try:
        p_ratings=soup.find_all('div',class_="XQDdHH")
    except:
        p_ratings="NA"
    try:
        p_prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
    except:
        p_prices="NA"
    try:
        p_reviews=soup.find_all('span',class_="Wphh3N")
    except:
        p_reviews="NA"


     # Extract data for each product
    for i in p_names:
        Names.append(i.text)
    for j in p_ratings:
        Ratings.append(j.text)
    for k in p_prices:
        Prices.append(k.text)
    for l in p_reviews:
        Reviews.append(l.text)
print("~ All Products Extraction Complete...")
# print(f"Names:{len(Names)}")
# print(f"Ratings:{len(Ratings)}")
# print(f"Prices:{len(Prices)}")
# print(f"Reviews:{len(Reviews)}")
products=len(Names)
print(f"Total Products: {products}")
time.sleep(2)
min_length=min(len(Names),len(Ratings),len(Prices),len(Reviews))
Names=Names[:min_length]
Ratings=Ratings[:min_length]
Prices=Prices[:min_length]
Reviews=Reviews[:min_length]

details={"Product Name":Names,
      "Rating":Ratings,
      "Price":Prices,
      "Review":Reviews}
# print(details)

print(f"~ Feature extraction complete...")
print()
time.sleep(0.100)
print("~ Initiating data conversion......")
time.sleep(3)
os.system("cls")
df = pd.DataFrame(details)
print(f"{'='*10} {products} Products of Data Table {'='*10}")
print(f"{"*"*30}~ Conversion complete....... {"*"*30}")
print()
print(df)
print()
print(f"{"*"*30}~ Web Scraping Complete......{"*"*30}")
time.sleep(5)
os.system('cls')
filename=input("Please  Give You Filename: ")
df.to_csv(f'{filename}.csv', header=True, index=False)
file = open(f'{filename}.json',  mode='w', encoding='utf-8')
file.write(json.dumps(details,ensure_ascii=True))
print()
print("storing to CSV file....")
time.sleep(3)
os.system('cls')
print("CSV File storing completed.")
time.sleep(2)
os.system('cls')
print("storing to JSON file....")
time.sleep(3)
os.system('cls')
print("JSON File storing completed")
time.sleep(2)
os.system('cls')
print("Successfully Completed Web Scraping.")