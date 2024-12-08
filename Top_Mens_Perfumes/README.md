# 📚 **Perfume24x7 Men's Collection Web Scraping Project** 🌐

## 🌟 **Project Overview**
This project involves **web scraping** data from the [Perfume24x7 Men's Collection](https://www.perfume24x7.com/collections/mens-collection) website. The goal is to extract detailed information about men's perfumes, including their names, ratings, and prices, and store this data in a structured format (CSV file). This project demonstrates practical web scraping techniques using **Python**.

---

## 📌 **Key Features**
- Scrapes perfume data, including:
  - 🖋 **Name** of the perfume.
  - ⭐ **Rating** of the perfume.
  - 💰 **Price** of the perfume.
- Automatically handles pagination to extract data across multiple pages.
- Saves the data into a **CSV file** (`top_mens_perfume.csv`) for further analysis.

---

## 🔧 **Technologies Used**
- **Python** 💾
  - Libraries: 
    - `requests` – for sending HTTP requests.
    - `BeautifulSoup` – for parsing and navigating HTML content.
    - `pandas` – for data manipulation and exporting.
- **Perfume24x7** – the data source for the project.

---

## 🗂 **Project Structure**
```plaintext
├── web_scraping_perfume.py  # Main Python script for web scraping
├── top_mens_perfume.csv     # Output file containing scraped data
└── README.md                # Documentation file
```

---

## 🚀 **How It Works**
1. **Send HTTP Request**:
   - The script uses `requests` to fetch HTML content of the Perfume24x7 website.
2. **Parse HTML**:
   - The `BeautifulSoup` library parses the HTML to extract relevant data like perfume names, ratings, and prices.
3. **Handle Pagination**:
   - A loop iterates through multiple pages of the website dynamically to gather all products.
4. **Store Data**:
   - Extracted data is appended to a list and converted into a **CSV file** using `pandas`.

---

## 🔎 **Output**
- **top_mens_perfume.csv**: Contains three columns:
  - `Name`: Name of the perfume.
  - `Rating`: Average rating of the perfume (if available).
  - `Price`: Price of the perfume (if available).

---

## 📊 **Sample Data**
| Name                        | Rating | Price       |
|-----------------------------|--------|-------------|
| Fragrance A                 | 4.5    | $49.99      |
| Fragrance B                 | 4.2    | $39.99      |
| Fragrance C                 | None   | $29.99      |

---

## ⚙️ **Setup Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name/web-scraping-perfumes.git
   cd web-scraping-perfumes
   ```
2. **Install Dependencies**:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. **Run the Script**:
   ```bash
   python web_scraping_perfume.py
   ```
4. **Check the Output**:
   - Open the `top_mens_perfume.csv` file to view the scraped data.

---

## 🏆 **Learning Outcomes**
- Gained hands-on experience with **HTML parsing** and **data extraction**.
- Improved understanding of Python libraries for web scraping and data manipulation.
- Enhanced skills in exporting structured data for analysis.

---

## 📢 **Contact**
If you have any questions or suggestions, please reach out via GitHub issues or email me at `sdavaras2@gitam.in`.

---