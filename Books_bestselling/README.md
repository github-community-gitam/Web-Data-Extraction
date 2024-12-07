

---

## 📚 Best-Selling Books Web Scraper

Welcome to the **Best-Selling Books Web Scraper** project! This repository demonstrates how to extract data from the internet using Python and convert it into a structured format for analysis. We focus on scraping book titles and their prices from an online bookstore. 🛒✨

---

## 📝 **Project Overview**

This project is a practical implementation of web scraping techniques to extract data from a webpage. The data includes:
- Book names 📖  
- Prices 💰  

The extracted data is saved as a **CSV file** for further analysis or usage. This project is ideal for understanding the fundamentals of **web scraping** with Python libraries like `requests` and `BeautifulSoup`.

---

## 🌟 **Key Features**

- **Dynamic Data Extraction:** Scrapes book titles and prices from an online bookstore.  
- **Data Structuring:** Converts the scraped data into a **pandas DataFrame**.  
- **File Export:** Saves the data in CSV format for further use.  
- **Debugging Support:** Handles missing or incomplete data gracefully with error messages.  

---

## 🛠️ **Technologies Used**

- **Python:** Programming language for data scraping and manipulation.  
- **requests:** For sending HTTP requests to the webpage.  
- **BeautifulSoup:** For parsing HTML content and extracting data.  
- **pandas:** For organizing and saving data into CSV files.  

---

## 📂 **Project Structure**

```
📦 Best-Selling Books Web Scraper
├── main.py                # Python script for web scraping
├── books_bestselling.csv  # Output CSV file
├── README.md              # Project documentation
```

---

## ⚙️ **How It Works**

1. **HTTP Request:** The script sends a request to the bookstore webpage using the `requests` library.  
2. **HTML Parsing:** Parses the webpage's content with `BeautifulSoup` to locate the required data elements (book names and prices).  
3. **Data Extraction:** Loops through the HTML structure to extract book names and prices.  
4. **Data Structuring:** Stores the extracted data in a pandas DataFrame.  
5. **File Export:** Saves the structured data as a CSV file named `books_bestselling.csv`.  

---

## 🖼️ **Output**

The final CSV file contains two columns:
1. **Book Name**  
2. **Price**

### Sample Output:
| Book Name                | Price   |  
|--------------------------|---------|  
| The Great Gatsby         | ₹300.00 |  
| To Kill a Mockingbird    | ₹250.00 |  
| 1984                     | ₹400.00 |  

---

## 📊 **Sample Data**

```csv
Book Name,Price
The Great Gatsby,₹300.00
To Kill a Mockingbird,₹250.00
1984,₹400.00
```

---

## 🛠️ **Setup Instructions**

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/bestselling-books-web-scraper.git
   cd bestselling-books-web-scraper
   ```
2. Install the required dependencies:  
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. Run the script:  
   ```bash
   python main.py
   ```
4. Check the generated `books_bestselling.csv` file in the project directory.

---

## 📚 **Learning Outcomes**

- Understanding web scraping concepts and best practices.  
- Working with Python libraries: `requests`, `BeautifulSoup`, and `pandas`.  
- Handling missing or incomplete data during web scraping.  
- Exporting and structuring data for analysis.  

---

## 📩 **Contact**

If you have any questions or suggestions, please reach out via GitHub issues or email me at `mmudundi@student.gitam.edu`.

---



