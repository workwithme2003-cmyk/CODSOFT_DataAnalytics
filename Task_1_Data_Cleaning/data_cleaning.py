import os
import pandas as pd
import numpy as np

def generate_raw_dataset(filepath):
    """Generates a realistic raw dataset with intentional data quality issues."""
    np.random.seed(42)
    n = 150
    
    data = {
        'Transaction_ID': [f'TXN-{1000 + i}' for i in range(n)],
        'Customer_ID': [f'CUST-{np.random.randint(100, 130)}' for _ in range(n)],
        'Customer_Age': [np.random.choice([25, 34, 45, 19, 52, -5, None, 120, '30']) for _ in range(n)],
        'Gender': [np.random.choice(['Male', 'Female', 'M', 'F', ' female ', None]) for _ in range(n)],
        'Product_Category': [np.random.choice(['Electronics', 'elec', 'ELECTRONICS', 'Clothing', 'clothing ', 'Home & Kitchen', None]) for _ in range(n)],
        'Purchase_Amount': [np.random.choice(['$150.50', '299.99', '$45.00', 'INVALID', None, '$1200.00', '89.99']) for _ in range(n)],
        'Payment_Method': [np.random.choice(['Credit Card', 'credit card', 'PayPal', 'Cash', None]) for _ in range(n)],
        'Transaction_Date': [np.random.choice(['2023-01-15', '15/01/2023', '2023-02-20', '2023-03-10', 'INVALID_DATE', None]) for _ in range(n)],
        'Satisfaction_Score': [np.random.choice([1, 2, 3, 4, 5, None, 10]) for _ in range(n)]
    }
    
    df = pd.DataFrame(data)
    
    # Introduce duplicate rows
    duplicates = df.iloc[:10].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    
    df.to_csv(filepath, index=False)
    print(f"Raw dataset generated and saved to '{filepath}' with {len(df)} rows.")
    return df


def inspect_dataset(df, stage_name="Raw Data"):
    """Prints structural inspection of the dataframe."""
    print(f"\n==========================================")
    print(f"       INSPECTING: {stage_name}")
    print(f"==========================================")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumn Data Types & Missing Values:")
    info_df = pd.DataFrame({
        'Dtype': df.dtypes,
        'Null_Count': df.isnull().sum(),
        'Null_Percentage': (df.isnull().sum() / len(df) * 100).round(2)
    })
    print(info_df)
    
    num_duplicates = df.duplicated().sum()
    print(f"\nTotal Duplicate Records: {num_duplicates}")


def clean_dataset(raw_filepath, clean_filepath):
    """Loads, cleans, and transforms raw dataset."""
    print("\n--- STEP 1: Loading Dataset ---")
    df = pd.read_csv(raw_filepath)
    inspect_dataset(df, "Raw Uncleaned Dataset")
    
    print("\n--- STEP 2: Cleaning Duplicate Records ---")
    initial_rows = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"Removed {initial_rows - len(df)} exact duplicate rows. Remaining: {len(df)}")
    
    print("\n--- STEP 3: Standardizing Column Names & Strings ---")
    df.columns = df.columns.str.strip().str.title()
    
    # Clean Product_Category
    if 'Product_Category' in df.columns:
        df['Product_Category'] = df['Product_Category'].astype(str).str.strip().str.title()
        category_map = {
            'Elec': 'Electronics',
            'Electronics': 'Electronics',
            'Clothing': 'Clothing',
            'Home & Kitchen': 'Home & Kitchen',
            'None': 'Unknown',
            'Nan': 'Unknown'
        }
        df['Product_Category'] = df['Product_Category'].map(lambda x: category_map.get(x, 'Unknown'))
        
    # Clean Gender
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].astype(str).str.strip().str.title()
        gender_map = {'M': 'Male', 'Male': 'Male', 'F': 'Female', 'Female': 'Female'}
        df['Gender'] = df['Gender'].map(lambda x: gender_map.get(x, 'Unknown'))

    # Clean Payment_Method
    if 'Payment_Method' in df.columns:
        df['Payment_Method'] = df['Payment_Method'].astype(str).str.strip().str.title()
        df['Payment_Method'] = df['Payment_Method'].replace({'Nan': 'Unknown', 'None': 'Unknown'})

    print("\n--- STEP 4: Correcting Numeric Data Types & Validating Range ---")
    # Clean Purchase_Amount
    df['Purchase_Amount'] = df['Purchase_Amount'].astype(str).str.replace('$', '', regex=False).str.strip()
    df['Purchase_Amount'] = pd.to_numeric(df['Purchase_Amount'], errors='coerce')
    # Impute missing Purchase_Amount with median
    median_amount = df['Purchase_Amount'].median()
    df['Purchase_Amount'] = df['Purchase_Amount'].fillna(median_amount).round(2)
    print(f"Cleaned Purchase_Amount (imputed missing with median: ${median_amount:.2f})")

    # Clean Customer_Age
    df['Customer_Age'] = pd.to_numeric(df['Customer_Age'], errors='coerce')
    # Filter out unreasonable ages (<18 or >100) as NaN
    df.loc[(df['Customer_Age'] < 18) | (df['Customer_Age'] > 100), 'Customer_Age'] = np.nan
    median_age = df['Customer_Age'].median()
    df['Customer_Age'] = df['Customer_Age'].fillna(median_age).astype(int)
    print(f"Cleaned Customer_Age (imputed invalid/missing with median age: {int(median_age)})")

    # Clean Satisfaction_Score
    df['Satisfaction_Score'] = pd.to_numeric(df['Satisfaction_Score'], errors='coerce')
    df.loc[(df['Satisfaction_Score'] < 1) | (df['Satisfaction_Score'] > 5), 'Satisfaction_Score'] = np.nan
    median_score = df['Satisfaction_Score'].median()
    df['Satisfaction_Score'] = df['Satisfaction_Score'].fillna(median_score).astype(int)
    print(f"Cleaned Satisfaction_Score (bounded 1-5, imputed missing with median: {int(median_score)})")

    print("\n--- STEP 5: Parsing & Standardizing Datetime ---")
    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], errors='coerce', format='mixed')
    # Forward fill or fill missing dates with most frequent date
    mode_date = df['Transaction_Date'].mode()[0]
    df['Transaction_Date'] = df['Transaction_Date'].fillna(mode_date)
    print(f"Parsed Transaction_Date into standard YYYY-MM-DD format.")

    print("\n--- STEP 6: Final Verification & Saving ---")
    inspect_dataset(df, "Cleaned & Processed Dataset")
    
    df.to_csv(clean_filepath, index=False)
    print(f"\nSUCCESS: Cleaned dataset saved as CSV to '{clean_filepath}'")
    return df


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(base_dir, "raw_dataset.csv")
    clean_path = os.path.join(base_dir, "cleaned_dataset.csv")
    
    # Generate raw noisy data
    generate_raw_dataset(raw_path)
    
    # Run data cleaning workflow
    clean_df = clean_dataset(raw_path, clean_path)
