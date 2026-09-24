import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CODEALPHA DATA ANALYTICS INTERNSHIP - TASK 2
# EXPLORATORY DATA ANALYSIS
# ============================================================

print("=" * 60)
print("CODEALPHA TASK 2 - EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# ============================================================
# 1. LOAD DATASET
# ============================================================

print("\nLoading dataset...")

file_path = "books_dataset.csv"

if not os.path.exists(file_path):
    print("ERROR: books_dataset.csv not found!")
    exit()

df = pd.read_csv(file_path)

print("Dataset loaded successfully.")


# ============================================================
# 2. DATASET INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


# ============================================================
# 3. FIRST 10 ROWS
# ============================================================

print("\n" + "=" * 60)
print("FIRST 10 ROWS")
print("=" * 60)

print(df.head(10).to_string(index=False))


# ============================================================
# 4. MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

print(missing_values)


# ============================================================
# 5. DUPLICATE ROWS
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print("Duplicate rows:", duplicate_count)


# ============================================================
# 6. DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Convert Price to numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")


# Handle Rating correctly
# The current dataset already contains numeric ratings 1-5.
if pd.api.types.is_numeric_dtype(df["Rating"]):

    df["Rating_Numeric"] = pd.to_numeric(
        df["Rating"],
        errors="coerce"
    )

else:

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["Rating_Numeric"] = df["Rating"].map(rating_map)


# Remove invalid rows
df = df.dropna(
    subset=[
        "Title",
        "Price",
        "Rating_Numeric",
        "Availability"
    ]
)


# Remove duplicate rows
df = df.drop_duplicates()


print("Cleaned dataset shape:", df.shape)


# ============================================================
# 7. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(
    df[
        [
            "Price",
            "Rating_Numeric"
        ]
    ].describe()
)


# ============================================================
# 8. PRICE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("PRICE ANALYSIS")
print("=" * 60)

print("\nMinimum Price:")
print(round(df["Price"].min(), 2))

print("\nMaximum Price:")
print(round(df["Price"].max(), 2))

print("\nAverage Price:")
print(round(df["Price"].mean(), 2))

print("\nMedian Price:")
print(round(df["Price"].median(), 2))


# ============================================================
# 9. RATING ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("RATING ANALYSIS")
print("=" * 60)

rating_counts = (
    df["Rating_Numeric"]
    .value_counts()
    .sort_index()
)

print("\nRating Counts:")
print(rating_counts)


# ============================================================
# 10. AVERAGE PRICE BY RATING
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE PRICE BY RATING")
print("=" * 60)

average_price_by_rating = (
    df.groupby("Rating_Numeric")["Price"]
    .mean()
    .sort_index()
)

print(average_price_by_rating)


# ============================================================
# 11. TOP 10 MOST EXPENSIVE BOOKS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 MOST EXPENSIVE BOOKS")
print("=" * 60)

top_expensive = (
    df[
        [
            "Title",
            "Price"
        ]
    ]
    .sort_values(
        by="Price",
        ascending=False
    )
    .head(10)
)

print(top_expensive.to_string(index=False))


# ============================================================
# 12. TOP 10 CHEAPEST BOOKS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 CHEAPEST BOOKS")
print("=" * 60)

top_cheap = (
    df[
        [
            "Title",
            "Price"
        ]
    ]
    .sort_values(
        by="Price",
        ascending=True
    )
    .head(10)
)

print(top_cheap.to_string(index=False))


# ============================================================
# 13. AVAILABILITY ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("AVAILABILITY ANALYSIS")
print("=" * 60)

availability_counts = (
    df["Availability"]
    .value_counts()
)

print(availability_counts)


# ============================================================
# 14. CREATE OUTPUT FOLDER
# ============================================================

output_folder = "eda_outputs"

os.makedirs(
    output_folder,
    exist_ok=True
)


# ============================================================
# 15. CHART 1 - PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price"],
    bins=20,
    edgecolor="black"
)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "price_distribution.png"
    )
)

plt.close()


# ============================================================
# 16. CHART 2 - RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 6))

rating_counts.plot(
    kind="bar"
)

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "rating_distribution.png"
    )
)

plt.close()


# ============================================================
# 17. CHART 3 - PRICE BY RATING
# ============================================================

plt.figure(figsize=(8, 6))

sns.boxplot(
    x="Rating_Numeric",
    y="Price",
    data=df
)

plt.title("Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Price")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "price_by_rating.png"
    )
)

plt.close()


# ============================================================
# 18. CHART 4 - TOP 10 EXPENSIVE BOOKS
# ============================================================

plt.figure(figsize=(12, 7))

top_expensive_plot = top_expensive.sort_values(
    by="Price",
    ascending=True
)

plt.barh(
    top_expensive_plot["Title"],
    top_expensive_plot["Price"]
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "top_10_expensive_books.png"
    )
)

plt.close()


# ============================================================
# 19. CHART 5 - AVERAGE PRICE BY RATING
# ============================================================

plt.figure(figsize=(8, 6))

average_price_by_rating.plot(
    kind="bar"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "average_price_by_rating.png"
    )
)

plt.close()


# ============================================================
# 20. CHART 6 - AVAILABILITY DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 6))

availability_counts.plot(
    kind="bar"
)

plt.title("Book Availability Distribution")
plt.xlabel("Availability")
plt.ylabel("Number of Books")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "availability_distribution.png"
    )
)

plt.close()


# ============================================================
# 21. CHART 7 - CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(8, 6))

correlation_data = df[
    [
        "Price",
        "Rating_Numeric"
    ]
].corr()

sns.heatmap(
    correlation_data,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Price and Rating Correlation")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "correlation_heatmap.png"
    )
)

plt.close()


# ============================================================
# 22. SAVE CLEANED DATASET
# ============================================================

cleaned_file = os.path.join(
    output_folder,
    "cleaned_books_dataset.csv"
)

df.to_csv(
    cleaned_file,
    index=False
)


# ============================================================
# 23. PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nAverage Price:")
print(round(df["Price"].mean(), 2))

print("\nAverage Rating:")
print(round(df["Rating_Numeric"].mean(), 2))

print("\nMost Common Rating:")

most_common_rating = (
    df["Rating_Numeric"]
    .mode()
)

if not most_common_rating.empty:
    print(int(most_common_rating.iloc[0]))
else:
    print("No rating available")


# ============================================================
# 24. OUTPUT FILES
# ============================================================

print("\n" + "=" * 60)
print("GENERATED FILES")
print("=" * 60)

for file_name in sorted(os.listdir(output_folder)):
    print(file_name)


# ============================================================
# 25. COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)