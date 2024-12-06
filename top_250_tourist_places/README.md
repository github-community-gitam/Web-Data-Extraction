# Tourist places Web Scraping Project 🌍✨

## 📜 **Project Overview**
This project involves scraping data from the **Top 250 tourist places in the World** webpage. The goal is to extract information about famous attractions, including their names, likes, and dislikes, and store this data in a structured format (CSV file). The project demonstrates real-world web scraping techniques using Python, focusing on data extraction, cleaning, and storage.

---
## 📌 **Key Features**
The script extracts:
- 🏰 **Place Name**: The name of the attraction.
- 👍 **Likes**: Number of people who liked the attraction.
- 👎 **Dislikes**: Number of people who disliked the attraction.

The data is saved into a CSV file named `famous_attractions117.csv` for further analysis. 

---
## 🛠️ **Technologies Used**
- **Python** 🐍
  - `requests`: To send HTTP requests and retrieve the webpage content.
  - `BeautifulSoup`: For parsing and navigating the HTML structure.
  - `pandas`: For data manipulation and exporting to CSV.

- **ListChallenges.com**: The practice website used for this project.

---
## 📂 **Project Structure**
```plaintext
├── attractions_scraper.py  # Main Python script for web scraping
├── famous_attractions117.csv  # Output file containing scraped data
└── README.md  # Documentation file
```
---
## 🚀 **How It Works**
1. **Send HTTP Request**:  
   The script uses the `requests` library to send a GET request to fetch the HTML content of the target URL.

2. **Parse HTML**:  
   BeautifulSoup parses the HTML to extract the required data fields, including:
   - Attraction name.
   - Number of likes and dislikes (adjusted based on the page structure).

3. **Extract Data**:  
   Loops through the HTML elements to scrape:
   - Place names from `<div>` tags with class `"item-name"`.
   - Likes and dislikes from the appropriate sibling tags.

4. **Store Data**:  
   Extracted data is stored in lists, which are then converted into a structured **pandas DataFrame** and saved to a CSV file.

---
## 🔍 **Output**
**CSV File: `famous_attractions117.csv`**  
The file contains three columns:
1. **Place Name**: Name of the attraction.
2. **Likes**: Count of likes.
3. **Dislikes**: Count of dislikes.

--- 
### 📊 **Sample Data**
---
| Place Name       | Likes | Dislikes |
|------------------|-------|----------|
| Eiffel Tower     | 1200  | 30       |
| Great Wall       | 1100  | 20       |
| Statue of Liberty| 950   | 25       |

---
## ⚙️ **Setup Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name/web-scraping-attractions.git
   cd web-scraping-attractions
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

3. **Run the Script**:
   ```bash
   python attractions_scraper.py
   ```

4. **Check the Output**:  
   Open the `famous_attractions117.csv` file to view the scraped data.

---
## 🏆 **Learning Outcomes**
- Practical experience in HTML parsing and data extraction.
- Improved understanding of web scraping libraries and their functionality.
- Enhanced skills in storing and analyzing structured data using **pandas**.

---
## 📬 **Contact**
If you have any questions or suggestions, please reach out via GitHub issues or email me at `vadibhat@gitam.in`.

---
Enjoy discovering the world’s top attractions! 🌏✨