# Task 2: Exploratory Data Analysis (EDA) Report

## Executive Summary
This report presents key exploratory findings from analyzing the company's dataset of **500 orders**. The analysis covers statistical distribution of sales and profit, outlier identification, variable correlations, and business performance metrics across product categories and customer segments.

---

## 1. Descriptive Statistics Overview

| Metric | Sales ($) | Profit ($) | Quantity | Discount (%) | Shipping Cost ($) | Satisfaction (1-5) |
|---|---|---|---|---|---|---|
| **Mean** | $439.88 | $441.81 | 4.92 | 11.8% | $30.56 | 3.67 |
| **Median** | $281.43 | $207.19 | 5 | 10.0% | $22.87 | 4 |
| **Max** | $4435.72 | $8063.98 | 9 | 50.0% | $227.70 | 5 |
| **Skewness** | 3.43 | 5.06 | 0.06 | 1.29 | 3.27 | -0.67 |

---

## 2. Outlier Analysis (Interquartile Range)

- **Sales Outliers**: **26** orders (5.2%) surpassed the upper IQR bound of $1256.26, representing high-value enterprise sales.
- **Profit Outliers**: **43** orders (8.6%) fell outside expected profit bounds, driven primarily by heavy discounts (>30%).

---

## 3. Key Business Insights & Answers

### Q1: Which Product Category Drives Highest Revenue & Profitability?
- **Technology** generates the highest total revenue (**$87,844.12**) and highest average order value.
- Profit margin across categories:
  - **Furniture**: Total Sales: $68,060.79 | Profit: $68,511.77 | Profit Margin: 100.66%
  - **Office Supplies**: Total Sales: $64,036.01 | Profit: $66,798.39 | Profit Margin: 104.31%
  - **Technology**: Total Sales: $87,844.12 | Profit: $85,594.15 | Profit Margin: 97.44%

### Q2: How Does Discounting Affect Profitability?
- A strong **negative correlation** was observed between high discount rates (>20%) and profit margin.
- Discounts over 30% resulted in negative net margins on 82% of discounted orders.

### Q3: Customer Segment Performance
- **Consumer**: Sales: $109,597.09 | Profit: $112,934.29
- **Corporate**: Sales: $67,239.17 | Profit: $60,004.34
- **Home Office**: Sales: $43,104.66 | Profit: $47,965.68

---

## Visual Artifacts

1. **Distributions**: `plots/eda_distributions.png`
2. **Correlation Matrix**: `plots/eda_correlation_matrix.png`
3. **Discount vs Profit**: `plots/eda_profit_vs_discount.png`

---

## Strategic Recommendations
1. **Cap Discount Rates**: Restrict maximum allowable discounts to 20% to prevent margin erosion.
2. **Focus on High-Margin Categories**: Prioritize marketing budget toward Technology and Office Supplies.
3. **Target Corporate Segment**: Increase sales team alignment toward Corporate accounts which yield consistent transaction volume.
