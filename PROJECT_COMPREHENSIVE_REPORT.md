# CodSoft Data Analytics Internship - Master Comprehensive Project Report

---

## 📌 Executive Summary

This document serves as the **Master Comprehensive Report** for the **CodSoft Data Analytics Virtual Internship** (Batch C14, July 25 – August 25, 2026). It contains end-to-end documentation of all 5 Data Analytics tasks, detailing project requirements, technical architecture, implementation workflows, empirical results, and strategic business outcomes.

---

## 🛠️ Project Requirements & Prerequisites ("What We Needed")

### 1. Software & Technical Environment
- **Programming Language**: Python 3.13 / Miniconda Python
- **Data Manipulation & Analytics**: `pandas`, `numpy`
- **Visualization Libraries**: `matplotlib`, `seaborn`, `plotly`
- **Machine Learning**: `scikit-learn` (`StandardScaler`, `KMeans`)
- **Web Extraction**: `beautifulsoup4`, `requests`
- **Web App Dashboard**: `streamlit` (>=1.57)
- **Data Export Formats**: CSV, Excel (`openpyxl`), PNG charts, Markdown reports (`.md`)

---

## 📋 Comprehensive Task Breakdown

---

### 🧹 TASK 1: DATA CLEANING & PREPROCESSING

#### 1. What We Needed
- Import raw, unstructured transaction data with real-world flaws (missing values, dirty string formats, duplicate entries, invalid age ranges, unformatted dates).
- Clean, deduplicate, format data types, impute nulls, and export a production-ready CSV dataset.

#### 2. How We Implemented
- **Script**: [`Task_1_Data_Cleaning/data_cleaning.py`](file:///c:/Projects/Codesoft/Task_1_Data_Cleaning/data_cleaning.py)
- **Raw Data Generation**: Created [`raw_dataset.csv`](file:///c:/Projects/Codesoft/Task_1_Data_Cleaning/raw_dataset.csv) (160 rows) containing missing values, whitespace noise, `$150.50` string amounts, negative ages (`-5`), invalid satisfaction scores (`10`), and 10 exact duplicate rows.
- **Cleaning Workflow**:
  - **Deduplication**: Removed 10 exact duplicate rows via `df.drop_duplicates()`.
  - **String Standardization**: Stripped leading/trailing whitespaces and mapped messy categories (`'elec'`, `'ELECTRONICS'`) to `'Electronics'`.
  - **Numeric Type Conversion**: Stripped `$` symbols using string regex replacement and converted `Purchase_Amount` to float. Imputed missing purchase amounts using the column median (`$150.50`).
  - **Invalid Range Filtering**: Filtered out invalid ages (`<18` or `>100`) and satisfaction scores outside `1-5`, replacing invalid entries with median values.
  - **Datetime Parsing**: Standardized mixed date strings into clean ISO `YYYY-MM-DD` timestamps.

#### 3. What We Achieved
- Successfully generated and exported [`cleaned_dataset.csv`](file:///c:/Projects/Codesoft/Task_1_Data_Cleaning/cleaned_dataset.csv) (150 clean rows, 9 columns).
- Achieved **0% null values** and **0 duplicate records** across the entire dataset.

---

### 📊 TASK 2: EXPLORATORY DATA ANALYSIS (EDA)

#### 1. What We Needed
- Load an e-commerce sales dataset, calculate descriptive statistics, explore feature distributions, analyze variable correlations, detect statistical outliers, and answer key business questions.

#### 2. How We Implemented
- **Script**: [`Task_2_EDA/eda_analysis.py`](file:///c:/Projects/Codesoft/Task_2_EDA/eda_analysis.py)
- **Dataset**: [`Task_2_EDA/sales_dataset.csv`](file:///c:/Projects/Codesoft/Task_2_EDA/sales_dataset.csv) (500 records).
- **Statistical Summary**: Calculated Mean, Median, Standard Deviation, Min, Max, **Skewness**, and **Kurtosis** across numerical features (`Sales`, `Profit`, `Quantity`, `Discount`, `Shipping_Cost`, `Customer_Rating`).
- **Outlier Detection**: Applied the **Interquartile Range (IQR)** method ($Q1 - 1.5 \times IQR$ to $Q3 + 1.5 \times IQR$) to identify extreme values.
- **Visualization Suite**: Saved publication-grade visual charts in [`Task_2_EDA/plots/`](file:///c:/Projects/Codesoft/Task_2_EDA/plots/):
  - `eda_distributions.png`: Histograms & box plots for sales, profit, and category breakdowns.
  - `eda_correlation_matrix.png`: Heatmap showing feature correlations.
  - `eda_profit_vs_discount.png`: Scatter plot evaluating margin loss from excessive discounting.

#### 3. What We Achieved
- **Outliers Detected**: Identified 26 Sales outliers (5.2%) and 43 Profit outliers (8.6%).
- **Business Findings**: Discovered that discount rates exceeding **20%** severely eroded profit margins, causing negative net returns on 82% of heavily discounted items.
- **Report Created**: Authored executive findings in [`Task_2_EDA/eda_report.md`](file:///c:/Projects/Codesoft/Task_2_EDA/eda_report.md).

---

### 📈 TASK 3: DATA VISUALIZATION DASHBOARD

#### 1. What We Needed
- Design static publication-grade visualizations (bar, line, pie, scatter, histograms) and build an interactive web dashboard.

#### 2. How We Implemented
- **Static Visualizations Script**: [`Task_3_Data_Visualization/generate_visualizations.py`](file:///c:/Projects/Codesoft/Task_3_Data_Visualization/generate_visualizations.py)
  - Generated high-resolution PNG charts in [`Task_3_Data_Visualization/plots/`](file:///c:/Projects/Codesoft/Task_3_Data_Visualization/plots/).
- **Interactive Streamlit Dashboard**: [`Task_3_Data_Visualization/dashboard_app.py`](file:///c:/Projects/Codesoft/Task_3_Data_Visualization/dashboard_app.py)
  - Built using official **Streamlit Skill Guidelines**:
    - **Card Containers (`st.container(border=True)`)**: Wrapped charts, metric grids, and data tables into clean cards.
    - **Metric Sparklines (`st.metric(..., chart_data=..., chart_type="line")`)**: Displayed real-time inline trend lines on Total Revenue and Total Profit metric cards.
    - **Dynamic Plotly Charts**: Interactive monthly revenue trend line chart, category bar chart, segment market share donut chart, and discount scatter plot.
    - **Interactive Filtering**: Multi-select filters for Region, Category, and Segment in the sidebar.
    - **Data Export**: Integrated CSV download button (`st.download_button`).

#### 3. What We Achieved
- Delivered an interactive web app running locally at `http://localhost:8501`.
- Enabled instant visual exploration and custom data filtering for executive stakeholders.

---

### 🎯 TASK 4: CUSTOMER DATA ANALYSIS & SEGMENTATION

#### 1. What We Needed
- Analyze customer demographic and transaction behavior, perform customer segmentation, identify top-tier customer groups, and provide strategic marketing recommendations.

#### 2. How We Implemented
- **Script**: [`Task_4_Customer_Data_Analysis/customer_analysis.py`](file:///c:/Projects/Codesoft/Task_4_Customer_Data_Analysis/customer_analysis.py)
- **Dataset**: [`Task_4_Customer_Data_Analysis/customer_transactions.csv`](file:///c:/Projects/Codesoft/Task_4_Customer_Data_Analysis/customer_transactions.csv) (250 customer profiles).
- **RFM Feature Engineering**: Calculated **Recency** (days since last purchase), **Frequency** (total orders), and **Monetary Value** (total spending).
- **Machine Learning Clustering**:
  - Normalized RFM features using `StandardScaler`.
  - Trained a **K-Means Machine Learning Clustering model ($k=4$)** to group customers into 4 behavioral segments:
    1. **VIP Champions** ($143.8k total spend, $3,508 avg spend per customer).
    2. **Loyal High-Value** ($79.1k total spend).
    3. **At-Risk Customers** ($87.8k total spend, high recency >260 days).
    4. **Occasional/Budget Shoppers** ($67.1k total spend).

#### 3. What We Achieved
- Plotted RFM scatter matrices and customer count/revenue bar charts in [`Task_4_Customer_Data_Analysis/plots/`](file:///c:/Projects/Codesoft/Task_4_Customer_Data_Analysis/plots/).
- Formulated targeted marketing strategies (VIP ambassador rewards, automated 90-day win-back emails, bundle cross-selling) in [`Task_4_Customer_Data_Analysis/customer_insights_report.md`](file:///c:/Projects/Codesoft/Task_4_Customer_Data_Analysis/customer_insights_report.md).

---

### 🌐 TASK 5: WEB DATA EXTRACTION & ANALYSIS

#### 1. What We Needed
- Scrape product data from a public website using `BeautifulSoup` & `requests`, structure the scraped records into clean datasets, export to CSV/Excel, and perform exploratory data analysis.

#### 2. How We Implemented
- **Scraper Script**: [`Task_5_Web_Data_Extraction/web_scraper.py`](file:///c:/Projects/Codesoft/Task_5_Web_Data_Extraction/web_scraper.py)
- **Analysis Script**: [`Task_5_Web_Data_Extraction/scraper_analysis.py`](file:///c:/Projects/Codesoft/Task_5_Web_Data_Extraction/scraper_analysis.py)
- **Scraping Workflow**:
  - Scraped 60 product listings across 3 catalog pages from `http://books.toscrape.com/`.
  - Parsed Title, Price (£), Star Rating (1 to 5), Stock Availability, and Source URL.
  - Used regular expressions (`re.search(r'\d+\.\d+|\d+', price_str)`) to reliably extract numerical prices across varying currency encodings.
  - Included a robust fallback mechanism for offline compatibility.

#### 3. What We Achieved
- Successfully extracted 60 products and exported structured datasets to [`scraped_products.csv`](file:///c:/Projects/Codesoft/Task_5_Web_Data_Extraction/scraped_products.csv) and [`scraped_products.xlsx`](file:///c:/Projects/Codesoft/Task_5_Web_Data_Extraction/scraped_products.xlsx).
- Analyzed price distribution across star rating categories and generated visual charts in [`Task_5_Web_Data_Extraction/plots/`](file:///c:/Projects/Codesoft/Task_5_Web_Data_Extraction/plots/).

---

## 📁 Repository Directory Map

```text
c:\Projects\Codesoft/
│
├── PROJECT_COMPREHENSIVE_REPORT.md    # Master Comprehensive Report (This File)
├── README.md                           # Master GitHub Repository Readme
├── requirements.txt                    # Project Dependencies
│
├── Task_1_Data_Cleaning/               # Task 1 Folder
│   ├── raw_dataset.csv
│   ├── cleaned_dataset.csv
│   └── data_cleaning.py
│
├── Task_2_EDA/                         # Task 2 Folder
│   ├── sales_dataset.csv
│   ├── eda_analysis.py
│   ├── eda_report.md
│   └── plots/
│
├── Task_3_Data_Visualization/          # Task 3 Folder
│   ├── generate_visualizations.py
│   ├── dashboard_app.py                # Upgraded Streamlit App
│   └── plots/
│
├── Task_4_Customer_Data_Analysis/      # Task 4 Folder
│   ├── customer_transactions.csv
│   ├── customer_analysis.py
│   ├── customer_insights_report.md
│   └── plots/
│
└── Task_5_Web_Data_Extraction/         # Task 5 Folder
    ├── web_scraper.py
    ├── scraper_analysis.py
    ├── scraped_products.csv
    ├── scraped_products.xlsx
    └── plots/
```

---

## 🚀 Execution & Verification Summary

All task scripts were executed and verified cleanly on system terminal:

```bash
# Task 1 Execution
python Task_1_Data_Cleaning/data_cleaning.py

# Task 2 Execution
python Task_2_EDA/eda_analysis.py

# Task 3 Static Visualizations
python Task_3_Data_Visualization/generate_visualizations.py

# Task 3 Interactive Web Dashboard
streamlit run Task_3_Data_Visualization/dashboard_app.py

# Task 4 Execution
python Task_4_Customer_Data_Analysis/customer_analysis.py

# Task 5 Execution
python Task_5_Web_Data_Extraction/web_scraper.py
python Task_5_Web_Data_Extraction/scraper_analysis.py
```

---

## 📢 Submission Checklist

1. **GitHub Repository**: ✅ **COMPLETED** — Live at [https://github.com/workwithme2003-cmyk/CODSOFT_DataAnalytics](https://github.com/workwithme2003-cmyk/CODSOFT_DataAnalytics).
2. **LinkedIn Video Demo**: Record a 1-2 minute video of the running Streamlit dashboard (`streamlit run Task_3_Data_Visualization/dashboard_app.py`) and code. Post on LinkedIn with `@codsoft` and `#codsoft #cip #dataanalytics`.
3. **Task Submission Form**: Fill the official CodSoft form ([forms.gle/RGRHmH7LBKUGWrfb6](https://forms.gle/RGRHmH7LBKUGWrfb6)) between **August 11 and August 25, 2026**.
