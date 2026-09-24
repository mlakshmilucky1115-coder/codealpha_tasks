import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CODEALPHA DATA ANALYTICS INTERNSHIP - TASK 3
# DATA VISUALIZATION
# ============================================================

print("=" * 70)
print("CODEALPHA DATA ANALYTICS INTERNSHIP - TASK 3")
print("DATA VISUALIZATION")
print("=" * 70)


# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = "books_dataset.csv"

if not os.path.exists(file_path):
    print(f"ERROR: {file_path} not found.")
    raise SystemExit

df = pd.read_csv(file_path)

print("\nDataset loaded successfully.")
print(f"Dataset shape: {df.shape}")


# ============================================================
# 2. DISPLAY BASIC INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# ============================================================
# 3. DATA CLEANING
# ============================================================

# Convert Price to numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")


# Convert Rating into numeric values
if pd.api.types.is_numeric_dtype(df["Rating"]):
    df["Rating_Numeric"] = pd.to_numeric(
        df["Rating"], errors="coerce"
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
df = df.dropna(subset=["Price", "Rating_Numeric"])

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned dataset shape:", df.shape)


# ============================================================
# 4. CREATE OUTPUT DIRECTORY
# ============================================================

output_dir = "visualizations"

os.makedirs(output_dir, exist_ok=True)


# ============================================================
# 5. SET VISUALIZATION STYLE
# ============================================================

sns.set_theme(style="whitegrid")


# ============================================================
# VISUALIZATION 1
# PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Price"],
    bins=20,
    kde=True
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "price_distribution.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 2
# RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.countplot(
    x=df["Rating_Numeric"]
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "rating_distribution.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 3
# AVERAGE PRICE BY RATING
# ============================================================

average_price = (
    df.groupby("Rating_Numeric")["Price"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=average_price,
    x="Rating_Numeric",
    y="Price"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "average_price_by_rating.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 4
# PRICE BY RATING - BOXPLOT
# ============================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Rating_Numeric",
    y="Price"
)

plt.title("Book Price Distribution by Rating")
plt.xlabel("Rating")
plt.ylabel("Price")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "price_by_rating_boxplot.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 5
# AVAILABILITY DISTRIBUTION
# ============================================================

availability_counts = df["Availability"].value_counts()

plt.figure(figsize=(10, 6))

sns.barplot(
    x=availability_counts.index,
    y=availability_counts.values
)

plt.title("Book Availability Distribution")
plt.xlabel("Availability")
plt.ylabel("Number of Books")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "availability_distribution.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 6
# TOP 10 MOST EXPENSIVE BOOKS
# ============================================================

top_10 = (
    df.nlargest(10, "Price")
    .sort_values("Price", ascending=True)
)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_10,
    x="Price",
    y="Title"
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price")
plt.ylabel("Book Title")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "top_10_expensive_books.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 7
# PRICE VS RATING SCATTER PLOT
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Rating_Numeric",
    y="Price",
    alpha=0.6
)

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "price_vs_rating.png"),
    dpi=300
)

plt.close()


# ============================================================
# VISUALIZATION 8
# CORRELATION HEATMAP
# ============================================================

correlation_data = df[
    ["Price", "Rating_Numeric"]
].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_data,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Price and Rating")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "correlation_heatmap.png"),
    dpi=300
)

plt.close()


# ============================================================
# 6. SAVE VISUALIZATION SUMMARY DATA
# ============================================================

summary = pd.DataFrame({
    "Metric": [
        "Total Books",
        "Average Price",
        "Median Price",
        "Minimum Price",
        "Maximum Price",
        "Average Rating",
        "Most Common Rating"
    ],
    "Value": [
        len(df),
        round(df["Price"].mean(), 2),
        round(df["Price"].median(), 2),
        round(df["Price"].min(), 2),
        round(df["Price"].max(), 2),
        round(df["Rating_Numeric"].mean(), 2),
        int(df["Rating_Numeric"].mode()[0])
    ]
})

summary.to_csv(
    os.path.join(output_dir, "visualization_summary.csv"),
    index=False
)


# ============================================================
# 7. PRINT KEY INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("KEY VISUALIZATION INSIGHTS")
print("=" * 70)

print(f"\nTotal books analyzed: {len(df)}")

print(
    f"Average book price: {df['Price'].mean():.2f}"
)

print(
    f"Median book price: {df['Price'].median():.2f}"
)

print(
    f"Minimum book price: {df['Price'].min():.2f}"
)

print(
    f"Maximum book price: {df['Price'].max():.2f}"
)

print(
    f"Average rating: {df['Rating_Numeric'].mean():.2f}"
)

print(
    f"Most common rating: "
    f"{int(df['Rating_Numeric'].mode()[0])}"
)

print("\nAverage price by rating:")

print(
    average_price.to_string(index=False)
)


# ============================================================
# 8. DISPLAY GENERATED FILES
# ============================================================

print("\n" + "=" * 70)
print("GENERATED VISUALIZATION FILES")
print("=" * 70)

for filename in sorted(os.listdir(output_dir)):
    print(f" - {filename}")


print("\n" + "=" * 70)
print("DATA VISUALIZATION COMPLETED SUCCESSFULLY")
print("=" * 70)