import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

# ============================================================
# CODEALPHA TASK 1 - WEB SCRAPING
# Project: Book Data Web Scraper
# ============================================================

# Website URL
base_url = "https://books.toscrape.com/"

# List to store scraped book data
books = []

# Start with the first page
next_url = base_url

# ============================================================
# SCRAPE ALL PAGES
# ============================================================

while next_url:

    print(f"Scraping: {next_url}")

    try:
        # Send request to website
        response = requests.get(
            next_url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        # Stop if request was unsuccessful
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Error accessing page: {e}")
        break

    # Convert HTML into BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    book_items = soup.select("article.product_pod")

    # ========================================================
    # EXTRACT BOOK INFORMATION
    # ========================================================

    for book in book_items:

        # Book title
        title = book.h3.a.get("title", "").strip()

        # Price
        price = book.select_one(".price_color").get_text(strip=True)

        # Availability
        availability = book.select_one(
            ".availability"
        ).get_text(" ", strip=True)

        # Rating
        rating_element = book.select_one("p.star-rating")

        if rating_element:
            rating_class = rating_element.get("class", [])
            rating = rating_class[1] if len(rating_class) > 1 else "Unknown"
        else:
            rating = "Unknown"

        # Relative book URL
        relative_url = book.h3.a.get("href", "")

        # Convert relative URL into complete URL
        full_url = urljoin(next_url, relative_url)

        # Add book information to list
        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": full_url
        })

    # ========================================================
    # FIND NEXT PAGE
    # ========================================================

    next_button = soup.select_one("li.next a")

    if next_button:
        next_url = urljoin(
            next_url,
            next_button.get("href")
        )
    else:
        next_url = None

    # Small delay between requests
    time.sleep(0.2)


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(books)


# ============================================================
# REMOVE DUPLICATES
# ============================================================

df.drop_duplicates(
    subset="Title",
    inplace=True
)


# ============================================================
# CLEAN PRICE
# ============================================================

df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)


# ============================================================
# CONVERT RATING WORDS TO NUMBERS
# ============================================================

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)


# ============================================================
# CLEAN AVAILABILITY
# ============================================================

df["Availability"] = (
    df["Availability"]
    .str.replace("\n", " ", regex=False)
    .str.strip()
)


# ============================================================
# REMOVE ROWS WITH MISSING IMPORTANT DATA
# ============================================================

df.dropna(
    subset=["Title", "Price", "Rating"],
    inplace=True
)


# ============================================================
# RESET INDEX
# ============================================================

df.reset_index(drop=True, inplace=True)


# ============================================================
# SAVE DATASET
# ============================================================

df.to_csv(
    "books_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 60)
print("WEB SCRAPING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"Total books scraped: {len(df)}")

print("\nDataset columns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())

print("\nPrice statistics:")
print(df["Price"].describe())

print("\nRating distribution:")
print(df["Rating"].value_counts().sort_index())

print("\nDataset saved as:")
print("books_dataset.csv")

print("=" * 60)