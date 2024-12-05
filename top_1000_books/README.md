Here’s a detailed and professional README.md file for your project:

---

# 📚 **Books to Scrape Web Scraping Project** 🌐

## 🌟 **Project Overview**
This project focuses on **web scraping** the popular [Books to Scrape](https://books.toscrape.com/) website. The goal is to extract detailed information about books, including their titles, prices, and links, and store this data in a structured format (CSV file). The project is part of a data science initiative to demonstrate real-world web scraping techniques using **Python**.

---

## 📌 **Key Features**
- Scrapes book data, including:
  - 📝 **Title** of the book.
  - 💰 **Price** of the book.
  - 🔗 **Link** to the book’s page.
- Automatically handles pagination to extract data across multiple pages.
- Saves the data into a **CSV file** (`book.csv`) for further analysis.

---

## 🛠️ **Technologies Used**
- **Python** 🐍
  - Libraries: 
    - `requests` – for sending HTTP requests.
    - `BeautifulSoup` – for parsing and navigating HTML content.
    - `pandas` – for data manipulation and exporting.
- **Books to Scrape** – a practice website for web scraping.

---

## 📂 **Project Structure**
```plaintext
├── books_to_scrape.py  # Main Python script for web scraping
├── book.csv            # Output file containing scraped data
└── README.md           # Documentation file
```

---

## 🚀 **How It Works**
1. **Send HTTP Request**:
   - The script uses `requests` to fetch HTML content of the Books to Scrape website.
2. **Parse HTML**:
   - The `BeautifulSoup` library parses the HTML to extract relevant data like book titles, prices, and links.
3. **Handle Pagination**:
   - A loop iterates through multiple pages of the website until a **404 error** is encountered, indicating the end of the catalog.
4. **Store Data**:
   - Extracted data is appended to a list and converted into a **CSV file** using `pandas`.



## 🔍 **Output**
- **book.csv**: Contains three columns:
  - `Title`: Name of the book.
  - `link`: Relative link to the book's page.
  - `price`: Price of the book.

---

## 📊 **Sample Data**
| Title                                  | Link                             | Price    |
|----------------------------------------|----------------------------------|----------|
| A Light in the Attic                   | catalogue/a-light-in-the-attic_9 | £51.77   |
| Tipping the Velvet                     | catalogue/tipping-the-velvet_999 | £53.74   |
| Soumission                             | catalogue/soumission_998         | £50.10   |

---

## ⚙️ **Setup Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name/web-scraping-books.git
   cd web-scraping-books
   ```
2. **Install Dependencies**:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. **Run the Script**:
   ```bash
   python books_to_scrape.py
   ```
4. **Check the Output**:
   - Open the `book.csv` file to view the scraped data.

---



## 🏆 **Learning Outcomes**
- Gained hands-on experience with **HTML parsing** and **data extraction**.
- Improved understanding of Python libraries for web scraping and data manipulation.
- Enhanced skills in exporting structured data for analysis.

---

## 📬 **Contact**
If you have any questions or suggestions, please reach out via GitHub issues or email me at `gkrishna3@gitam.in`.

---

Enjoy exploring the world of books! 📚✨