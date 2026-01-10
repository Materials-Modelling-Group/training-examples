# Python Alternative to PSPP
# Demonstrates equivalent analyses using pandas and scipy

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

print("Python Statistical Analysis")
print("==========================\n")

# Create sample data
np.random.seed(42)
data = pd.DataFrame({
    'id': range(1, 101),
    'age': np.random.randint(20, 60, 100),
    'gender': np.random.choice(['M', 'F'], 100),
    'score': np.random.randint(60, 100, 100)
})

print("Sample Data:")
print(data.head())
print(f"\nDataset: {len(data)} rows, {len(data.columns)} columns\n")

# === Descriptive Statistics ===

print("=== Descriptive Statistics ===\n")
print(data.describe())

print("\nDetailed statistics for 'score':")
print(f"  Mean: {data['score'].mean():.2f}")
print(f"  Median: {data['score'].median():.2f}")
print(f"  Std Dev: {data['score'].std():.2f}")
print(f"  Min: {data['score'].min()}")
print(f"  Max: {data['score'].max()}")
print(f"  Range: {data['score'].max() - data['score'].min()}")

# === Frequency Tables ===

print("\n=== Frequency Tables ===\n")

print("Gender frequencies:")
print(data['gender'].value_counts())
print("\nGender proportions:")
print(data['gender'].value_counts(normalize=True))

# === Group Comparisons ===

print("\n=== Group Statistics ===\n")

print("Score by Gender:")
group_stats = data.groupby('gender')['score'].agg([
    ('Count', 'count'),
    ('Mean', 'mean'),
    ('Std', 'std'),
    ('Min', 'min'),
    ('Max', 'max')
])
print(group_stats)

# === T-Test ===

print("\n=== Independent Samples T-Test ===\n")

male_scores = data[data['gender'] == 'M']['score']
female_scores = data[data['gender'] == 'F']['score']

t_stat, p_value = stats.ttest_ind(male_scores, female_scores)

print(f"Male mean: {male_scores.mean():.2f} (n={len(male_scores)})")
print(f"Female mean: {female_scores.mean():.2f} (n={len(female_scores)})")
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.3f}")
print(f"Result: {'Significant' if p_value < 0.05 else 'Not significant'} at α=0.05")

# === Correlation ===

print("\n=== Correlation Analysis ===\n")

corr, p = stats.pearsonr(data['age'], data['score'])
print(f"Correlation between age and score: {corr:.3f}")
print(f"p-value: {p:.3f}")

# === Crosstabulation ===

print("\n=== Crosstabulation ===\n")

# Create age groups
data['age_group'] = pd.cut(data['age'], bins=[0, 30, 45, 100], 
                           labels=['Young', 'Middle', 'Senior'])

# Crosstab
ct = pd.crosstab(data['gender'], data['age_group'])
print("Count:")
print(ct)

print("\nRow percentages:")
print(pd.crosstab(data['gender'], data['age_group'], normalize='index') * 100)

# Chi-square test
chi2, p, dof, expected = stats.chi2_contingency(ct)
print(f"\nChi-square statistic: {chi2:.3f}")
print(f"p-value: {p:.3f}")
print(f"Degrees of freedom: {dof}")

# === Linear Regression ===

print("\n=== Linear Regression ===\n")

from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(data['age'], data['score'])

print(f"Regression equation: score = {intercept:.2f} + {slope:.2f} * age")
print(f"R-squared: {r_value**2:.3f}")
print(f"p-value: {p_value:.3f}")

# === Visualization ===

print("\n=== Creating Visualizations ===\n")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histogram
axes[0, 0].hist(data['score'], bins=15, edgecolor='black')
axes[0, 0].set_title('Distribution of Scores')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')

# Box plot
data.boxplot(column='score', by='gender', ax=axes[0, 1])
axes[0, 1].set_title('Scores by Gender')
axes[0, 1].set_xlabel('Gender')
axes[0, 1].set_ylabel('Score')

# Scatter plot with regression line
axes[1, 0].scatter(data['age'], data['score'], alpha=0.5)
axes[1, 0].plot(data['age'], intercept + slope * data['age'], 'r-', linewidth=2)
axes[1, 0].set_title('Age vs Score')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Score')

# Bar plot
group_means = data.groupby('gender')['score'].mean()
axes[1, 1].bar(group_means.index, group_means.values)
axes[1, 1].set_title('Mean Scores by Gender')
axes[1, 1].set_xlabel('Gender')
axes[1, 1].set_ylabel('Mean Score')

plt.tight_layout()
plt.savefig('analysis_plots.png', dpi=300)
print("Saved plots to 'analysis_plots.png'")

plt.show()

print("\nAnalysis complete!")
