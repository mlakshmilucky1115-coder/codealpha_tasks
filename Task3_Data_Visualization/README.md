# CodeAlpha Data Visualization Project

## CodeAlpha Data Analytics Internship – Task 3: Data Visualization

This project demonstrates data visualization techniques using Python, Pandas, Matplotlib, and Seaborn.

The dataset contains information about books collected from the Books to Scrape website.

## Project Objective

The objective of this task is to transform the book dataset into meaningful visualizations that help identify patterns and relationships in:

- Book prices
- Book ratings
- Average price by rating
- Price distribution
- Price and rating relationship
- Price variation across ratings
- Most expensive books
- Book availability

## Dataset

The dataset contains 999 books with the following columns:

- Title
- Price
- Rating
- Availability
- URL

## Technologies Used

- Python 3.13
- Pandas
- Matplotlib
- Seaborn

## Visualizations Created

The project generates the following charts:

1. Price Distribution
2. Rating Distribution
3. Average Price by Rating
4. Top 10 Most Expensive Books
5. Price vs Rating
6. Price Distribution by Rating
7. Availability Distribution
8. Correlation Heatmap

## Key Insights

- Total books analyzed: 999
- Average book price: 35.07
- Median book price: 36.00
- Minimum book price: 10.00
- Maximum book price: 59.99
- Average rating: 2.92
- Most common rating: 1
- All 999 books are listed as in stock.

The average prices across ratings are relatively close:

| Rating | Average Price |
|--------|---------------|
| 1 Star | 34.56 |
| 2 Stars | 34.81 |
| 3 Stars | 34.69 |
| 4 Stars | 36.09 |
| 5 Stars | 35.39 |

## Project Structure

```text
CodeAlpha_Data_Visualization/
│
├── books_dataset.csv
├── visualization.py
├── README.md
├── requirements.txt
│
└── visualizations/
    ├── availability_distribution.png
    ├── average_price_by_rating.png
    ├── correlation_heatmap.png
    ├── price_by_rating_boxplot.png
    ├── price_distribution.png
    ├── price_vs_rating.png
    ├── rating_distribution.png
    ├── top_10_expensive_books.png
    └── visualization_summary.csv