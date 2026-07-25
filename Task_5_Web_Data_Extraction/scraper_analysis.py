import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'Segoe UI'

def analyze_scraped_data(csv_path, output_dir):
    """Performs analysis on extracted product data."""
    df = pd.read_csv(csv_path)
    plots_dir = os.path.join(output_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    print("\n--- SCRAPED DATA SUMMARY ---")
    print(f"Total Products Analyzed: {len(df)}")
    print(f"Average Product Price: £{df['Price_GBP'].mean():.2f}")
    print(f"Average Customer Rating: {df['Rating_Stars'].mean():.2f} / 5.0")
    
    price_by_rating = df.groupby('Rating_Stars')['Price_GBP'].agg(['mean', 'median', 'count']).reset_index()
    print("\nPrice Breakdown by Rating Stars:")
    print(price_by_rating)

    # Plot 1: Price Distribution & Box Plot by Rating
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    sns.histplot(df['Price_GBP'], kde=True, color='#2b5c8f', bins=15, ax=axes[0])
    axes[0].set_title("Scraped Product Price Distribution (£)", fontweight='bold')
    axes[0].set_xlabel("Price (£)")
    
    sns.boxplot(x='Rating_Stars', y='Price_GBP', data=df, palette='Blues', ax=axes[1])
    axes[1].set_title("Product Price vs Star Rating Class", fontweight='bold')
    axes[1].set_xlabel("Rating (Stars)")
    axes[1].set_ylabel("Price (£)")
    
    plt.tight_layout()
    plot_path = os.path.join(plots_dir, "scraped_data_analysis.png")
    plt.savefig(plot_path, dpi=300)
    plt.close()
    
    print(f"SUCCESS: Analysis plot saved to '{plot_path}'.")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "scraped_products.csv")
    analyze_scraped_data(data_path, base_dir)
