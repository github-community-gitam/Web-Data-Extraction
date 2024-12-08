import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.perfume24x7.com/collections/mens-collection?page=1"
response=requests.get(url)
response
soup=BeautifulSoup(response,'html.parser')
soup
products=soup.find_all('a',class_='grid-product__link')
products
perfumes=[]
for i in range(1,20):
  url=f"https://www.perfume24x7.com/collections/mens-collection?page={i}"
  response=requests.get(url)
  response=response.content
  soup=BeautifulSoup(response,'html.parser')
  for product in products:
      name = product.find('div', class_='grid-product__title grid-product__title--body').get_text(strip=True)
      rating_div = product.find('div', class_='jdgm-prev-badge')
      if rating_div:
          rating = rating_div.get('data-average-rating')
      price_element = product.find('span', class_='grid-product__price--original')
      if price_element:
        price = price_element.get_text(strip=True)
      perfumes.append([name,rating,price])
      df=pd.DataFrame(perfumes,columns=['Name','Rating','Price'])
df.to_csv('top_mens_perfume.csv')