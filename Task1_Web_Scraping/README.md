# CodeAlpha Web Scraping Project

## 📚 Book Data Web Scraping Using Python

### 📌 Project Overview

This project is developed as part of the CodeAlpha Data Analytics Internship – Task 1: Web Scraping.

The project uses Python, Requests, BeautifulSoup, and Pandas to collect book information from a public practice website and convert the scraped information into a structured CSV dataset.

### 🎯 Objectives

* Extract book information from web pages.
* Navigate through multiple pages automatically.
* Collect structured information from HTML.
* Clean and transform the collected data.
* Remove duplicate records.
* Create a reusable CSV dataset.

### 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

### 📊 Dataset

The scraper collected the following information:

| Column       | Description              |
| ------------ | ------------------------ |
| Title        | Name of the book         |
| Price        | Book price               |
| Rating       | Book rating from 1 to 5  |
| Availability | Availability status      |
| URL          | Complete URL of the book |

### 📈 Dataset Summary

* Total records: 999
* Total columns: 5
* Missing values: 0
* Duplicate records: 0

### 🔎 Web Scraping Process

The project follows these steps:

1. Connect to the public website using Requests.
2. Download the webpage HTML.
3. Parse the HTML using BeautifulSoup.
4. Identify book elements using HTML/CSS selectors.
5. Extract title, price, rating, availability, and URL.
6. Navigate through multiple pages using the Next button.
7. Remove duplicate records.
8. Clean price and rating values.
9. Store the data in a Pandas DataFrame.
10. Export the final dataset to CSV.

### 📁 Project Structure

```text
CodeAlpha_Web_Scraping/
│
├── scraper.py
├── books_dataset.csv
├── requirements.txt
└── README.md
```

### ▶️ How to Run the Project

#### 1. Clone or download the project

Open PowerShell in the project directory.

#### 2. Install required libraries

```bash
pip install -r requirements.txt
```

#### 3. Run the scraper

```bash
python scraper.py
```

#### 4. Output

After successful execution, the scraper creates:

```text
books_dataset.csv
```

### 💡 Key Features

* Multi-page web scraping
* Request error handling
* HTML parsing
* Data cleaning
* Duplicate removal
* Rating conversion
* Price conversion
* Complete URL generation
* CSV dataset generation

### 📌 Project Outcome

The final result is a structured dataset containing 999 book records collected through automated web scraping.

This dataset can be used for further data analysis and visualization projects.

### 👨‍💻 Internship

**Program:** CodeAlpha Data Analytics Internship

**Task:** Task 1 – Web Scraping

**Project:** Book Data Web Scraping Using Python and BeautifulSoup
