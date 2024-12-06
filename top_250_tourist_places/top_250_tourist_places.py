import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the webpage to scrape
url = "https://www.listchallenges.com/top-250-famous-attractions-in-the-world/vote"

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Lists to store the scraped data
places = []
likes = []
dislikes = []

# Find all the attraction entries
attractions = soup.find_all("div", class_="item-name")  # Adjust if necessary based on HTML structure

# Loop through each attraction to extract name, likes, and dislikes
for attraction in attractions:
    # Extract place name
    place_name = attraction.get_text(strip=True)
    places.append(place_name)
    
    # Find likes and dislikes, adjust based on actual HTML structure
    like_count = attraction.find_next("div", class_="h5 m").get_text(strip=True)
    dislike_count = attraction.find_next("div", class_="h5").get_text(strip=True)
    
    # Append to lists
    likes.append(like_count)
    dislikes.append(dislike_count)

# Create a DataFrame to store the data
df = pd.DataFrame({
    "Place Name": places,
    "Likes": likes,
    "Dislikes": dislikes
})

# Save the DataFrame to a CSV file
df.to_csv("tourist_places.csv", index=False)
print("Data has been saved to famous_attractions117.csv")