import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Styling setup
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'Segoe UI'

def generate_customer_dataset(filepath):
    """Generates synthetic customer transaction history."""
    np.random.seed(42)
    n_customers = 250
    
    customers = []
    for i in range(n_customers):
        cust_id = f"CUST-{1000 + i}"
        age = np.random.randint(18, 70)
        gender = np.random.choice(['Male', 'Female'], p=[0.48, 0.52])
        location = np.random.choice(['Urban', 'Suburban', 'Rural'], p=[0.5, 0.35, 0.15])

        # Cluster behavior generation
        behavior_type = np.random.choice(['VIP', 'Loyal', 'At-Risk', 'Budget'], p=[0.2, 0.35, 0.25, 0.2])
        
        if behavior_type == 'VIP':
            recency = np.random.randint(1, 30)
            frequency = np.random.randint(8, 25)
            monetary = np.random.uniform(1500, 5000)
        elif behavior_type == 'Loyal':
            recency = np.random.randint(10, 60)
            frequency = np.random.randint(4, 12)
            monetary = np.random.uniform(600, 1800)
        elif behavior_type == 'At-Risk':
            recency = np.random.randint(90, 365)
            frequency = np.random.randint(3, 10)
            monetary = np.random.uniform(700, 2500)
        else: # Budget
            recency = np.random.randint(40, 180)
            frequency = np.random.randint(1, 4)
            monetary = np.random.uniform(50, 400)
            
        customers.append({
            'Customer_ID': cust_id,
            'Age': age,
            'Gender': gender,
            'Location_Type': location,
            'Recency_Days': recency,
            'Frequency_Orders': frequency,
            'Monetary_Spend': np.round(monetary, 2)
        })
        
    df = pd.DataFrame(customers)
    df.to_csv(filepath, index=False)
    print(f"Customer dataset saved to '{filepath}' ({len(df)} records).")
    return df


def analyze_customers(csv_path, output_dir):
    """Executes customer RFM analysis, K-Means clustering, and report generation."""
    df = pd.read_csv(csv_path)
    plots_dir = os.path.join(output_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    print("\n--- STEP 1: RFM Feature Standardization ---")
    features = ['Recency_Days', 'Frequency_Orders', 'Monetary_Spend', 'Age']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[features])
    
    print("\n--- STEP 2: K-Means Customer Segmentation (k=4) ---")
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(scaled_features)
    
    # Map cluster indices to human-readable names based on Monetary & Frequency means
    cluster_means = df.groupby('Cluster')[['Monetary_Spend', 'Frequency_Orders', 'Recency_Days']].mean()
    print("Cluster Feature Means:")
    print(cluster_means)
    
    # Assign labels dynamically
    cluster_mapping = {}
    sorted_clusters = cluster_means.sort_values(by='Monetary_Spend', ascending=False).index
    cluster_mapping[sorted_clusters[0]] = "1. VIP Champions"
    cluster_mapping[sorted_clusters[1]] = "2. Loyal High-Value"
    cluster_mapping[sorted_clusters[2]] = "3. At-Risk Customers"
    cluster_mapping[sorted_clusters[3]] = "4. Occasional/Budget"
    
    df['Segment_Name'] = df['Cluster'].map(cluster_mapping)
    df = df.sort_values(by='Segment_Name')

    print("\n--- STEP 3: Segment Profiles & Summary ---")
    segment_summary = df.groupby('Segment_Name').agg(
        Customer_Count=('Customer_ID', 'count'),
        Avg_Age=('Age', 'mean'),
        Avg_Recency=('Recency_Days', 'mean'),
        Avg_Frequency=('Frequency_Orders', 'mean'),
        Avg_Spend=('Monetary_Spend', 'mean'),
        Total_Revenue=('Monetary_Spend', 'sum'),
        Revenue_Share=('Monetary_Spend', lambda x: (x.sum() / df['Monetary_Spend'].sum()) * 100)
    ).reset_index()
    print(segment_summary)

    print("\n--- STEP 4: Visual Reports Generation ---")
    # Plot 1: Segment Revenue & Count Comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    sns.barplot(data=segment_summary, x='Segment_Name', y='Total_Revenue', palette='Blues_r', ax=axes[0])
    axes[0].set_title("Total Revenue Contribution by Customer Segment", fontweight='bold')
    axes[0].set_ylabel("Total Revenue ($)")
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=20)
    
    sns.barplot(data=segment_summary, x='Segment_Name', y='Customer_Count', palette='Greens_r', ax=axes[1])
    axes[1].set_title("Customer Count per Segment", fontweight='bold')
    axes[1].set_ylabel("Number of Customers")
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=20)
    
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "customer_segments_summary.png"), dpi=300)
    plt.close()

    # Plot 2: RFM Scatter Matrix (Recency vs Monetary)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, x='Recency_Days', y='Monetary_Spend', 
        hue='Segment_Name', size='Frequency_Orders', sizes=(40, 250),
        palette='Set1', alpha=0.85
    )
    plt.title("Customer RFM Segmentation Matrix (Recency vs Spend)", fontweight='bold', fontsize=14)
    plt.xlabel("Recency (Days Since Last Order)")
    plt.ylabel("Total Monetary Spend ($)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "customer_rfm_scatter.png"), dpi=300)
    plt.close()

    # Generate customer_insights_report.md
    report_path = os.path.join(output_dir, "customer_insights_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"""# Task 4: Customer Data Analysis & Segmentation Report

## Executive Summary
Using **RFM (Recency, Frequency, Monetary) Modeling** and **K-Means Machine Learning Clustering**, we segmented a customer base of **{len(df)} customers** into 4 distinct behavioral segments. This analysis identifies high-value customer groups and delivers targeted marketing strategies to maximize lifetime value (LTV).

---

## Customer Segment Characteristics Summary

| Segment Name | Customer Count | Avg Age | Avg Recency (Days) | Avg Frequency (Orders) | Avg Spend ($) | Total Revenue ($) | Revenue Share (%) |
|---|---|---|---|---|---|---|---|
""")
        for _, row in segment_summary.iterrows():
            f.write(f"| **{row['Segment_Name']}** | {row['Customer_Count']} | {row['Avg_Age']:.1f} | {row['Avg_Recency']:.1f} | {row['Avg_Frequency']:.1f} | ${row['Avg_Spend']:,.2f} | ${row['Total_Revenue']:,.2f} | {row['Revenue_Share']:.1f}% |\n")

        f.write("""
---

## Key Segment Deep-Dives

### 1. VIP Champions (Top Value Group)
- **Profile**: Most frequent buyers with the highest average spend and recent interactions.
- **Value**: Contributes a disproportionate share of total revenue despite being a smaller segment.
- **Goal**: Retention, VIP exclusivity, and advocacy.

### 2. Loyal High-Value
- **Profile**: Regular repeat purchasers with steady transaction history.
- **Value**: Reliable, recurring baseline revenue stream.
- **Goal**: Upsell premium product bundles and launch loyalty tier incentives.

### 3. At-Risk Customers
- **Profile**: High historical spend but haven't purchased in 90+ days.
- **Risk**: Potential churn to competitors.
- **Goal**: Win-back campaigns with targeted reactivation discounts and personalized email triggers.

### 4. Occasional / Budget Shoppers
- **Profile**: Low transaction frequency and modest cart values.
- **Goal**: Drive first-to-second order conversion via low-friction offers.

---

## Actionable Marketing Strategies & Recommendations

1. **VIP Ambassador Program**:
   - Offer early access to newly launched products and dedicated customer support.
   - Introduce referral bonuses to leverage VIP customer advocacy.

2. **Automated Win-Back Triggers for At-Risk Customers**:
   - Implement automated email alerts at Day 60 and Day 90 post-purchase offering a 15% re-engagement voucher.

3. **Cross-Selling & Bundle Discounts for Loyal Segment**:
   - Target loyal customers with recommendations based on past category purchases to increase average order value (AOV).

---

## Generated Visualizations
- **Summary Charts**: `plots/customer_segments_summary.png`
- **RFM Scatter Plot**: `plots/customer_rfm_scatter.png`
""")

    print(f"\nSUCCESS: Customer Analysis complete. Report generated at '{report_path}'.")
    return df


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cust_data = os.path.join(base_dir, "customer_transactions.csv")
    generate_customer_dataset(cust_data)
    analyze_customers(cust_data, base_dir)
