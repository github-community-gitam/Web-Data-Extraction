import requests
from bs4 import BeautifulSoup
import pandas as pd
 
i=1
data=[]
proceed=True
while(proceed):
    url="https://books.toscrape.com/catalogue/page-"+str(i)+".html"
    req=requests.get(url)
    soup=BeautifulSoup(req.text,"html.parser")

    if soup.title.text=="404 Not Found":
        proceed=False
    else:
       find_books=soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
       for book in find_books:
           item={}
           item['Title']=book.find("img").attrs["alt"]

           item['link']=book.find("a").attrs["href"]
           item['price']=book.find("p",class_="price_color").text
           print(item['price'])
           data.append(item)  
    i=i+1
df=pd.DataFrame(data)
df.to_csv("books.csv")