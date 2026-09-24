import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# ============================================================
# CODEALPHA DATA ANALYTICS INTERNSHIP - TASK 4
# SENTIMENT ANALYSIS
# ============================================================

print("SENTIMENT ANALYSIS - CODEALPHA TASK 4")
print("=" * 60)


# ============================================================
# 1. DOWNLOAD VADER LEXICON
# ============================================================

try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    print("\nDownloading VADER lexicon...")
    nltk.download("vader_lexicon")


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("\nLoading dataset...")

df = pd.read_csv("cleaned_reviews.csv")

print("Dataset loaded successfully.")


# ============================================================
# 3. DATASET INFORMATION
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
# 4. DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# Remove rows with missing review text
df = df.dropna(subset=["cleaned_review"]).copy()

# Convert review text to string
df["cleaned_review"] = df["cleaned_review"].astype(str)

# Make sure review score is numeric
df["review_score"] = pd.to_numeric(
    df["review_score"],
    errors="coerce"
)

# Remove rows where review score is missing
df = df.dropna(subset=["review_score"]).copy()


print("\nDataset Shape After Removing Missing Reviews:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# 5. DUPLICATE CHECK AND REMOVAL
# ============================================================

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows Before Removal:")
print(duplicate_count)

# Remove duplicate rows
df = df.drop_duplicates().copy()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

print("\nDuplicate Rows After Removal:")
print(df.duplicated().sum())


# ============================================================
# 6. ORIGINAL SENTIMENT DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("ORIGINAL SENTIMENT DISTRIBUTION")
print("=" * 60)

sentiment_counts = df["sentiments"].value_counts()

print("\nSentiment Distribution:")
print(sentiment_counts)


# ============================================================
# 7. REVIEW SCORE DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("REVIEW SCORE DISTRIBUTION")
print("=" * 60)

score_counts = (
    df["review_score"]
    .value_counts()
    .sort_index()
)

print("\nReview Score Distribution:")
print(score_counts)


# ============================================================
# 8. AVERAGE REVIEW LENGTH BY SENTIMENT
# ============================================================

print("\n" + "=" * 60)
print("REVIEW LENGTH ANALYSIS")
print("=" * 60)

avg_length = (
    df.groupby("sentiments")["cleaned_review_length"]
    .mean()
)

print("\nAverage Review Length by Sentiment:")
print(avg_length)


# ============================================================
# 9. AVERAGE REVIEW SCORE BY SENTIMENT
# ============================================================

print("\n" + "=" * 60)
print("REVIEW SCORE BY SENTIMENT")
print("=" * 60)

avg_score = (
    df.groupby("sentiments")["review_score"]
    .mean()
)

print("\nAverage Review Score by Sentiment:")
print(avg_score)


# ============================================================
# 10. VADER SENTIMENT ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("VADER SENTIMENT ANALYSIS")
print("=" * 60)

# Create VADER analyzer
sia = SentimentIntensityAnalyzer()


# Calculate VADER compound score
df["vader_score"] = df["cleaned_review"].apply(
    lambda text: sia.polarity_scores(text)["compound"]
)


# ============================================================
# 11. CLASSIFY VADER SENTIMENT
# ============================================================

def classify_sentiment(score):

    if score >= 0.05:
        return "positive"

    elif score <= -0.05:
        return "negative"

    else:
        return "neutral"


df["vader_sentiment"] = df["vader_score"].apply(
    classify_sentiment
)


# ============================================================
# 12. VADER SENTIMENT DISTRIBUTION
# ============================================================

vader_counts = (
    df["vader_sentiment"]
    .value_counts()
)

print("\nVADER Sentiment Distribution:")
print(vader_counts)


# ============================================================
# 13. SAMPLE VADER RESULTS
# ============================================================

print("\n" + "=" * 60)
print("SAMPLE VADER RESULTS")
print("=" * 60)

print(
    df[
        [
            "cleaned_review",
            "vader_score",
            "vader_sentiment"
        ]
    ].head(10)
)


# ============================================================
# 14. VADER SCORE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("VADER SCORE STATISTICS")
print("=" * 60)

print("\nVADER Score Statistics:")
print(df["vader_score"].describe())


# ============================================================
# 15. SENTIMENT COMPARISON
# ============================================================

print("\n" + "=" * 60)
print("SENTIMENT COMPARISON")
print("=" * 60)

comparison = pd.crosstab(
    df["sentiments"],
    df["vader_sentiment"]
)

print("\nOriginal Sentiment vs VADER Sentiment:")
print(comparison)


# ============================================================
# 16. CREATE CHARTS FOLDER
# ============================================================

os.makedirs("charts", exist_ok=True)


# ============================================================
# 17. CHART - ORIGINAL SENTIMENT DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sentiment_plot_counts = (
    df["sentiments"]
    .value_counts()
    .reindex(
        ["negative", "neutral", "positive"],
        fill_value=0
    )
)

plt.bar(
    sentiment_plot_counts.index,
    sentiment_plot_counts.values
)

plt.title("Original Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "charts/sentiment_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 18. CHART - REVIEW SCORE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

score_plot_counts = (
    df["review_score"]
    .value_counts()
    .reindex([1, 2, 3, 4, 5], fill_value=0)
)

plt.bar(
    score_plot_counts.index.astype(str),
    score_plot_counts.values
)

plt.title("Review Score Distribution")
plt.xlabel("Review Score")
plt.ylabel("Number of Reviews")

# Add values above bars
for i, value in enumerate(score_plot_counts.values):
    plt.text(
        i,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "charts/review_score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 19. CHART - VADER SENTIMENT DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

vader_plot_counts = (
    df["vader_sentiment"]
    .value_counts()
    .reindex(
        ["negative", "neutral", "positive"],
        fill_value=0
    )
)

plt.bar(
    vader_plot_counts.index,
    vader_plot_counts.values
)

plt.title("VADER Sentiment Distribution")
plt.xlabel("VADER Sentiment")
plt.ylabel("Number of Reviews")

# Add values above bars
for i, value in enumerate(vader_plot_counts.values):
    plt.text(
        i,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "charts/vader_sentiment_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 20. CHART - VADER SCORE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["vader_score"],
    bins=30
)

plt.title("VADER Sentiment Score Distribution")
plt.xlabel("VADER Compound Score")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "charts/vader_score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 21. CHART - AVERAGE REVIEW SCORE BY SENTIMENT
# ============================================================

plt.figure(figsize=(8, 5))

avg_score_plot = (
    df.groupby("sentiments")["review_score"]
    .mean()
    .reindex(
        ["negative", "neutral", "positive"]
    )
)

plt.bar(
    avg_score_plot.index,
    avg_score_plot.values
)

plt.title("Average Review Score by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average Review Score")

# Add values above bars
for i, value in enumerate(avg_score_plot.values):
    plt.text(
        i,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "charts/average_score_by_sentiment.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 22. CHART - AVERAGE REVIEW LENGTH BY SENTIMENT
# ============================================================

plt.figure(figsize=(8, 5))

avg_length_plot = (
    df.groupby("sentiments")["cleaned_review_length"]
    .mean()
    .reindex(
        ["negative", "neutral", "positive"]
    )
)

plt.bar(
    avg_length_plot.index,
    avg_length_plot.values
)

plt.title("Average Review Length by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average Review Length")

# Add values above bars
for i, value in enumerate(avg_length_plot.values):
    plt.text(
        i,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "charts/average_review_length_by_sentiment.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 23. CHART - ORIGINAL VS VADER SENTIMENT
# ============================================================

comparison_plot = pd.crosstab(
    df["sentiments"],
    df["vader_sentiment"]
)

comparison_plot = comparison_plot.reindex(
    index=["negative", "neutral", "positive"],
    columns=["negative", "neutral", "positive"],
    fill_value=0
)

comparison_plot.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Original Sentiment vs VADER Sentiment")
plt.xlabel("Original Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.legend(title="VADER Sentiment")

plt.tight_layout()

plt.savefig(
    "charts/sentiment_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 24. SAVE SENTIMENT RESULTS
# ============================================================

output_columns = [
    "sentiments",
    "cleaned_review",
    "cleaned_review_length",
    "review_score",
    "vader_score",
    "vader_sentiment"
]

df[output_columns].to_csv(
    "sentiment_results.csv",
    index=False
)


# ============================================================
# 25. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("\nOriginal Dataset Rows:", 17340)

print("Missing Reviews Removed:", 3)

print("Duplicate Rows Removed:", duplicate_count)

print("Final Reviews Analyzed:", len(df))


print("\nOriginal Sentiment Counts:")
print(df["sentiments"].value_counts())


print("\nVADER Sentiment Counts:")
print(df["vader_sentiment"].value_counts())


print(
    "\nAverage VADER Score:",
    round(df["vader_score"].mean(), 4)
)


print("\nReview Score Counts:")
print(
    df["review_score"]
    .value_counts()
    .sort_index()
)


print("\nCharts saved in:")
print("charts/")


print("\nResults saved as:")
print("sentiment_results.csv")


print("\n" + "=" * 60)
print("SENTIMENT ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)