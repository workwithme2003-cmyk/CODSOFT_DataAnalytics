# Task 4: Customer Data Analysis & Segmentation Report

## Executive Summary
Using **RFM (Recency, Frequency, Monetary) Modeling** and **K-Means Machine Learning Clustering**, we segmented a customer base of **250 customers** into 4 distinct behavioral segments. This analysis identifies high-value customer groups and delivers targeted marketing strategies to maximize lifetime value (LTV).

---

## Customer Segment Characteristics Summary

| Segment Name | Customer Count | Avg Age | Avg Recency (Days) | Avg Frequency (Orders) | Avg Spend ($) | Total Revenue ($) | Revenue Share (%) |
|---|---|---|---|---|---|---|---|
| **1. VIP Champions** | 41 | 42.6 | 14.3 | 17.6 | $3,508.57 | $143,851.46 | 38.1% |
| **2. Loyal High-Value** | 46 | 44.8 | 264.8 | 5.7 | $1,720.39 | $79,138.05 | 20.9% |
| **3. At-Risk Customers** | 84 | 29.1 | 64.9 | 6.2 | $1,045.50 | $87,821.78 | 23.2% |
| **4. Occasional/Budget** | 79 | 56.6 | 66.7 | 5.4 | $849.90 | $67,141.76 | 17.8% |

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
