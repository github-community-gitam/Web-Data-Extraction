import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = "https://bookspringindia.in/collections/best-selling-books"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find the book elements
books = soup.find_all('div', class_='product-card')

# Step 4: Extract book names and prices
book_data = []
for book in books:
    title_element = book.find('div', class_='h4 grid-view-item_title product-card_title')
    price_element = book.find('span', class_='price-item price-item--regular')  # Update this based on your inspection

    # Check if title and price elements exist
    if title_element and price_element:
        title = title_element.text.strip()
        price = price_element.text.strip()
        book_data.append({'Book Name': title, 'Price': price})
    else:
        print("Title or Price not found for a book.")  # Debugging line

# Step 5: Create a DataFrame and save to CSV
df = pd.DataFrame(book_data)
df.to_csv('books_bestselling.csv', index=False)

print("Data has been scraped and saved to 'books_bestselling.csv'.")