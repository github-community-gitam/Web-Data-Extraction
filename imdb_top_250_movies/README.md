# IMDb Top 250 Movies Web Scraper 🎥📝

## Project Overview 📊
This project is a **web data extraction tool** that scrapes the IMDb Top 250 Movies list from IMDb’s website. It extracts key information about each movie, such as the title, rating, description, genre, and more, and converts the data into a structured format for further analysis.

### Purpose 💡
The goal of this project is to demonstrate how to use web scraping techniques to collect data from online sources using Python libraries like `requests` and `BeautifulSoup`. The extracted data can be used for insights, analysis, and applications in data science projects.

---

## Features 🔧
- Scrapes IMDb’s **Top 250 Movies** list.
- Extracts key movie details, including:
  - **Title**
  - **Rating**
  - **Rating Count**
  - **Description**
  - **Genre**
  - **Duration**
  - **Movie URL**
- Saves the scraped data into a CSV file for easy accessibility and analysis.
- Implements user-agent headers to mimic browser behavior and avoid bot detection.

---

## Tech Stack 🚀
- **Programming Language**: Python
- **Libraries Used**:
  - `requests`: For sending HTTP requests to the IMDb website.
  - `BeautifulSoup` (from `bs4`): For parsing and extracting HTML content.
  - `pandas`: For organizing the extracted data and saving it into a CSV file.

---

## How It Works 📝
1. **Setup**
   - Install the required Python packages:
     ```bash
     pip install requests beautifulsoup4
     ```
2. **Requesting Data**
   - Send an HTTP GET request to the IMDb Top 250 Movies page using a user-agent header to mimic browser behavior.
3. **Parsing HTML**
   - Parse the HTML response using `BeautifulSoup` to find the `script` tag containing structured JSON-LD data.
4. **Extracting Data**
   - Extract details of each movie from the JSON data, including title, rating, description, genre, etc.
5. **Saving Data**
   - Convert the extracted data into a structured `pandas` DataFrame and save it as a CSV file.
6. **Output**
   - Generate a file named `top_250_movies.csv` containing all the scraped movie details.

---

## File Structure 🗃️
- `imdb_top_250_movies.py`: The main Python script containing the web scraping logic.
- `top_250_movies.csv`: The output file containing the scraped IMDb Top 250 Movies data.

---

## Prerequisites 🔍
- Python 3.6+
- Libraries: `requests`, `beautifulsoup4`, `pandas`
- Internet connection to access the IMDb website.

---

## Usage Instructions 🔧
1. Clone or download the project.
2. Install the required libraries using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Python script:
   ```bash
   python imdb_top_250_movies.py
   ```
4. Find the `top_250_movies.csv` file in the project directory.

---

## Example Output 🌐
An example of the output CSV:
| Title                      | Rating | Genre            | Duration | Description                                      |
|----------------------------|--------|------------------|----------|------------------------------------------------|
| The Shawshank Redemption  | 9.3    | Drama            | PT142M   | Two imprisoned men bond over several years.    |
| The Godfather             | 9.2    | Crime, Drama     | PT175M   | The aging patriarch of an organized crime...   |

---

## Challenges Faced 😔
1. **Bot Detection**:
   - Used user-agent headers to bypass basic bot detection mechanisms.
2. **Parsing JSON-LD**:
   - Extracted structured movie data embedded within HTML using `BeautifulSoup`.

---

## Acknowledgments 🎉
This project is inspired by the wealth of information available on IMDb, and the techniques showcased here are for educational purposes only. IMDb’s data and services are copyright protected.

---

## Contributing 📚
Feel free to fork this repository and submit pull requests for new features, bug fixes, or improvements. Contributions are always welcome!

---

## Contact 📢
If you have any questions or suggestions, please reach out via GitHub issues or email me at `pchekuri@gitam.in`.


