# CodeAlpha Exploratory Data Analysis Project

## CodeAlpha Data Analytics Internship – Task 2: Exploratory Data Analysis

This project performs Exploratory Data Analysis (EDA) on a book dataset collected from Books to Scrape.

## Project Objective

The objective of this task is to analyze the collected book data, identify patterns and trends, clean the dataset, calculate statistical measures, and create visualizations.

## Dataset

The dataset contains information about **999 books**.

### Columns

* **Title** – Book title
* **Price** – Book price
* **Rating** – Book rating from 1 to 5
* **Availability** – Availability status
* **URL** – Book webpage URL

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Data Cleaning

The following steps were performed:

1. Loaded the CSV dataset.
2. Checked the dataset shape and data types.
3. Checked for missing values.
4. Checked for duplicate rows.
5. Converted the Price column to numeric format.
6. Validated the Rating column.
7. Created a numeric rating column.
8. Removed invalid and duplicate records.
9. Saved the cleaned dataset.

## Exploratory Data Analysis

The analysis includes:

* Dataset structure
* Missing-value analysis
* Duplicate analysis
* Descriptive statistics
* Price analysis
* Rating analysis
* Average price by rating
* Most expensive books
* Cheapest books
* Availability analysis
* Price and rating correlation

## Key Results

* Total books analyzed: **999**
* Missing values: **0**
* Duplicate rows: **0**
* Minimum price: **10.00**
* Maximum price: **59.99**
* Average price: **35.07**
* Median price: **36.00**
* Average rating: **2.92**
* All 999 books were listed as **In stock**

## Visualizations

The project generates the following charts:

1. Price Distribution
2. Rating Distribution
3. Price by Rating
4. Top 10 Most Expensive Books
5. Average Price by Rating
6. Availability Distribution
7. Price and Rating Correlation Heatmap

## Project Files

```text
CodeAlpha_EDA/
│
├── books_dataset.csv
├── eda.py
├── README.md
│
└── eda_outputs/
    ├── average_price_by_rating.png
    ├── availability_distribution.png
    ├── cleaned_books_dataset.csv
    ├── correlation_heatmap.png
    ├── price_by_rating.png
    ├── price_distribution.png
    ├── rating_distribution.png
    └── top_10_expensive_books.png
```

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

Run the EDA program:

```bash
python eda.py
```

The analysis results and visualizations will be saved in the `eda_outputs` folder.

## Internship

**Program:** CodeAlpha Data Analytics Internship

**Task:** Task 2 – Exploratory Data Analysis

**Author:** Lakshmi
