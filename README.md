# CodSoft Data Analytics Internship Repository

> 📊 **Live Streamlit Dashboard App**: [Open Streamlit Dashboard App Online](https://share.streamlit.io/workwithme2003-cmyk/codsoft_dataanalytics/main/Task_3_Data_Visualization/dashboard_app.py)
> 
> 🌐 **Live GitHub Pages Web Dashboard**: [Experience the Interactive Web Dashboard](https://workwithme2003-cmyk.github.io/CODSOFT_DataAnalytics/)
> 
> 📘 **Master Project Documentation**: Read the exhaustive breakdown in [PROJECT_COMPREHENSIVE_REPORT.md](PROJECT_COMPREHENSIVE_REPORT.md).

Welcome to my official submission repository for the **CodSoft Data Analytics Virtual Internship**. This repository contains complete implementations of all **5 Data Analytics Tasks**, including Python scripts, clean/processed datasets, statistical reports, publication-ready data visualizations, customer segmentation models, web scrapers, and an interactive Streamlit dashboard.

---

## 📁 Repository Structure

```
c:\Projects\Codesoft/
│
├── README.md                           # Master Project Documentation & Submission Guide
├── requirements.txt                    # Project Dependencies
│
├── Task_1_Data_Cleaning/               # Task 1: Data Cleaning & Preprocessing
│   ├── raw_dataset.csv                 # Raw dataset with nulls, duplicates, dirty formats
│   ├── cleaned_dataset.csv             # Cleaned, standardized, and imputed CSV output
│   └── data_cleaning.py                # Python script performing cleaning workflow
│
├── Task_2_EDA/                         # Task 2: Exploratory Data Analysis (EDA)
│   ├── sales_dataset.csv               # E-commerce transactional dataset
│   ├── eda_analysis.py                 # Statistical analysis & outlier detection script
│   ├── eda_report.md                   # Comprehensive Markdown Executive Findings Report
│   └── plots/                          # Generated distribution, heatmap, & scatter charts
│
├── Task_3_Data_Visualization/          # Task 3: Data Visualization Dashboard
│   ├── generate_visualizations.py      # Publication-ready static chart generation script
│   ├── dashboard_app.py                # Interactive Streamlit + Plotly Web Dashboard App
│   └── plots/                          # High-res PNG chart outputs
│
├── Task_4_Customer_Data_Analysis/      # Task 4: Customer Data Analysis & Segmentation
│   ├── customer_transactions.csv       # Customer transaction dataset
│   ├── customer_analysis.py            # RFM Scoring & K-Means Clustering Machine Learning script
│   ├── customer_insights_report.md     # Customer segment breakdown & marketing strategy report
│   └── plots/                          # RFM scatter matrix and segment comparison charts
│
└── Task_5_Web_Data_Extraction/         # Task 5: Web Data Extraction & Analysis
    ├── web_scraper.py                  # BeautifulSoup web scraper for product data
    ├── scraper_analysis.py             # Exploratory analysis on scraped web data
    ├── scraped_products.csv            # Extracted clean product dataset (CSV)
    ├── scraped_products.xlsx           # Extracted product dataset (Excel)
    └── plots/                          # Price vs Rating distribution charts
```

---

## 🚀 Tasks Overview & Deliverables

### 🧹 Task 1: Data Cleaning & Preprocessing
- **Objective**: Import raw data, identify missing values, duplicate records, structural inconsistencies, and invalid data types. Clean and prepare data using Pandas.
- **Key Deliverables**: `raw_dataset.csv`, `cleaned_dataset.csv`, and `data_cleaning.py`.
- **Techniques Used**: Null value imputation (median/mode), whitespace trim, string standardization, duplicate removal, datetime conversion, invalid range bounding.

---

### 📊 Task 2: Exploratory Data Analysis (EDA)
- **Objective**: Load dataset, compute descriptive statistics, examine feature distributions, identify correlation patterns, and detect outliers using the IQR method.
- **Key Deliverables**: `sales_dataset.csv`, `eda_analysis.py`, `eda_report.md`, and visual plot charts in `plots/`.
- **Key Insights**: Identified negative profit impact from discounts exceeding 20%, Technology as the top revenue category, and Corporate segment as the most consistent margin contributor.

---

### 📈 Task 3: Data Visualization & Interactive Dashboard
- **Objective**: Create multi-faceted static visualizations (bar, line, pie, histogram, scatter) and build an interactive web dashboard.
- **Key Deliverables**: `generate_visualizations.py`, `dashboard_app.py` (Streamlit app), and PNG plot exports.
- **Features**: Interactive sidebar filtering by Region, Category, Segment; real-time KPI metrics; Plotly Express dynamic charts; downloadable filtered CSV data.

---

### 🎯 Task 4: Customer Data Analysis & Segmentation
- **Objective**: Analyze customer demographic and purchasing behavior to segment customers and suggest marketing strategies.
- **Key Deliverables**: `customer_analysis.py`, `customer_insights_report.md`, and segmentation plots.
- **Methodology**: **RFM (Recency, Frequency, Monetary)** features standardized with `StandardScaler` and clustered using **K-Means Machine Learning (k=4)** into:
  1. *VIP Champions*
  2. *Loyal High-Value*
  3. *At-Risk Customers*
  4. *Occasional/Budget Shoppers*

---

### 🌐 Task 5: Web Data Extraction & Analysis
- **Objective**: Collect public web data using `BeautifulSoup` & `requests`, clean into structured dataset, and analyze trends.
- **Key Deliverables**: `web_scraper.py`, `scraper_analysis.py`, `scraped_products.csv`, `scraped_products.xlsx`.
- **Scraped Attributes**: Product Title, Price (£), Rating (Stars 1-5), Stock Availability, and Source URL.

---

## 🛠️ How to Run the Project

### 1. Installation & Environment Setup
Clone the repository and install requirements:
```bash
cd c:\Projects\Codesoft
python -m pip install -r requirements.txt
```

### 2. Executing Tasks
You can run any task script directly from terminal:

```bash
# Task 1: Data Cleaning
python Task_1_Data_Cleaning/data_cleaning.py

# Task 2: EDA Analysis
python Task_2_EDA/eda_analysis.py

# Task 3: Static Visualizations
python Task_3_Data_Visualization/generate_visualizations.py

# Task 4: Customer Data Analysis & Clustering
python Task_4_Customer_Data_Analysis/customer_analysis.py

# Task 5: Web Scraper & Scraping Analysis
python Task_5_Web_Data_Extraction/web_scraper.py
python Task_5_Web_Data_Extraction/scraper_analysis.py
```

### 3. Launching the Interactive Streamlit Dashboard
To launch the interactive dashboard in your web browser:
```bash
streamlit run Task_3_Data_Visualization/dashboard_app.py
```


