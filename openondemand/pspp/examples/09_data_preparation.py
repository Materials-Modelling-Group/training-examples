# Data Preparation for PSPP Analysis
# Demonstrates cleaning and exporting data for PSPP

import pandas as pd
import numpy as np

print("Data Preparation for PSPP")
print("=========================\n")

# Create sample dataset with various issues
np.random.seed(42)
n = 100

data = pd.DataFrame({
    'ID': range(1, n + 1),
    'Age': np.random.randint(18, 70, n),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], n),
    'Income': np.random.randint(20000, 100000, n),
    'Score': np.random.randint(50, 100, n),
    'Response': np.random.choice(['Yes', 'No', 'Maybe'], n)
})

# Introduce some missing values
data.loc[np.random.choice(data.index, 10), 'Income'] = np.nan
data.loc[np.random.choice(data.index, 5), 'Score'] = np.nan

print("Original data:")
print(data.head(10))
print(f"\nShape: {data.shape}")
print(f"\nMissing values:\n{data.isnull().sum()}")

# === Clean Data ===

print("\n" + "=" * 60)
print("Data Cleaning Steps")
print("=" * 60)

# 1. Handle missing values
print("\n1. Handling missing values...")
print(f"   Income: filling with median")
data['Income'].fillna(data['Income'].median(), inplace=True)

print(f"   Score: filling with mean")
data['Score'].fillna(data['Score'].mean(), inplace=True)

print(f"   After cleaning: {data.isnull().sum().sum()} missing values")

# 2. Recode categorical variables for PSPP
print("\n2. Recoding categorical variables...")

# Gender: Use single character codes
gender_map = {'Male': 'M', 'Female': 'F', 'Other': 'O'}
data['Gender'] = data['Gender'].map(gender_map)
print(f"   Gender recoded to: {data['Gender'].unique()}")

# Response: Use numeric codes
response_map = {'Yes': 1, 'No': 0, 'Maybe': 2}
data['Response_Code'] = data['Response'].map(response_map)
print(f"   Response recoded to numeric: {data['Response_Code'].unique()}")

# 3. Create age groups
print("\n3. Creating age groups...")
data['Age_Group'] = pd.cut(
    data['Age'],
    bins=[0, 30, 50, 100],
    labels=['Young', 'Middle', 'Senior']
)
print(f"   Age groups: {data['Age_Group'].value_counts().to_dict()}")

# Recode age groups to single characters for PSPP
age_group_map = {'Young': 'Y', 'Middle': 'M', 'Senior': 'S'}
data['Age_Group'] = data['Age_Group'].map(age_group_map)

# 4. Ensure proper variable names (no spaces, start with letter)
print("\n4. Checking variable names...")
print(f"   Column names: {list(data.columns)}")

# Rename if needed
data.columns = [col.replace(' ', '_').replace('-', '_') for col in data.columns]
print(f"   After cleanup: {list(data.columns)}")

# 5. Create income categories
print("\n5. Creating income categories...")
data['Income_Cat'] = pd.qcut(
    data['Income'],
    q=3,
    labels=['Low', 'Medium', 'High']
)
data['Income_Cat'] = data['Income_Cat'].map({'Low': 'L', 'Medium': 'M', 'High': 'H'})

# === Prepare Final Dataset ===

print("\n" + "=" * 60)
print("Preparing Final Dataset")
print("=" * 60)

# Select columns for PSPP
pspp_data = data[[
    'ID', 'Age', 'Gender', 'Income', 'Score',
    'Response_Code', 'Age_Group', 'Income_Cat'
]]

print("\nFinal dataset:")
print(pspp_data.head(10))
print(f"\nShape: {pspp_data.shape}")
print(f"\nData types:\n{pspp_data.dtypes}")

# === Export Data ===

print("\n" + "=" * 60)
print("Exporting Data")
print("=" * 60)

# Export to CSV for PSPP
output_file = 'data_for_pspp.csv'
pspp_data.to_csv(output_file, index=False)
print(f"\nExported to: {output_file}")

# Create a data dictionary
print("\nData Dictionary:")
print("-" * 60)
dictionary = {
    'ID': 'Participant ID (numeric)',
    'Age': 'Age in years (numeric)',
    'Gender': 'Gender (M=Male, F=Female, O=Other)',
    'Income': 'Annual income in dollars (numeric)',
    'Score': 'Test score 0-100 (numeric)',
    'Response_Code': 'Survey response (1=Yes, 0=No, 2=Maybe)',
    'Age_Group': 'Age category (Y=Young, M=Middle, S=Senior)',
    'Income_Cat': 'Income category (L=Low, M=Medium, H=High)'
}

for var, desc in dictionary.items():
    print(f"  {var:15s} : {desc}")

# === Create PSPP Syntax Template ===

print("\n" + "=" * 60)
print("PSPP Syntax Template")
print("=" * 60)

pspp_syntax = f"""
* PSPP Syntax for {output_file}
* Generated automatically

* Load data
DATA LIST FILE='{output_file}' free (',')
/ID Age Gender (A1) Income Score Response_Code Age_Group (A1) Income_Cat (A1).

* Variable labels
VARIABLE LABELS
ID 'Participant ID'
Age 'Age in years'
Gender 'Gender'
Income 'Annual Income'
Score 'Test Score'
Response_Code 'Survey Response'
Age_Group 'Age Category'
Income_Cat 'Income Category'.

* Value labels
VALUE LABELS
Gender 'M' 'Male' 'F' 'Female' 'O' 'Other'
/Response_Code 1 'Yes' 0 'No' 2 'Maybe'
/Age_Group 'Y' 'Young' 'M' 'Middle' 'S' 'Senior'
/Income_Cat 'L' 'Low' 'M' 'Medium' 'H' 'High'.

* Basic statistics
DESCRIPTIVES VARIABLES=Age Income Score
/STATISTICS=MEAN STDDEV MIN MAX.

FREQUENCIES VARIABLES=Gender Age_Group Income_Cat Response_Code.

* Save syntax
"""

syntax_file = 'analysis_template.sps'
with open(syntax_file, 'w') as f:
    f.write(pspp_syntax)

print(f"\nCreated PSPP syntax template: {syntax_file}")
print("\nSyntax preview:")
print(pspp_syntax)

print("\n" + "=" * 60)
print("Data preparation complete!")
print("=" * 60)
print(f"\nFiles created:")
print(f"  1. {output_file} - Data file for PSPP")
print(f"  2. {syntax_file} - PSPP syntax template")
print("\nYou can now use these files in PSPP or run from Python using subprocess")
