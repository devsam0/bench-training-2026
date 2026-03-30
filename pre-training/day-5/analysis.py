import pandas as pd

try:
  df = pd.read_csv('titanic.csv')
  original_row_count = len(df)
except FileNotFoundError:
  print("Error: titanic.csv not found. Please ensure it is in the same folder.")
  exit()

print("--- Titanic Data Analysis: Day 5 ---\n")

# 01. Survival Counts & Percentages
survived_counts = df['Survived'].value_counts()
survived_pct = df['Survived'].value_counts(normalize=True) * 100
print(f"01. Survival:\n    - Survived: {survived_counts[1]} ({survived_pct[1]:.2f}%)\n    - Died: {survived_counts[0]} ({survived_pct[0]:.2f}%)")

# 02. Survival Rate by Class
class_survival = df.groupby('Pclass')['Survived'].mean() * 100
print(f"\n02. Survival Rate by Class:\n{class_survival}")

# 03. Average Age (Survivors vs Non-Survivors)
avg_age_survival = df.groupby('Survived')['Age'].mean()
print(f"\n03. Average Age:\n    - Survivors: {avg_age_survival[1]:.2f}\n    - Non-survivors: {avg_age_survival[0]:.2f}")

# 04. Embarkation Port Survival Rate
# C = Cherbourg, Q = Queenstown, S = Southampton
embark_survival = df.groupby('Embarked')['Survived'].mean().sort_values(ascending=False)
print(f"\n04. Survival Rate by Port:\n{embark_survival}")

# 05. Handling Missing Ages
missing_ages = df['Age'].isnull().sum()
print(f"\n05. Missing Ages: {missing_ages}")
# Filling missing ages with the median age of their specific passenger class
df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))
print("    - Action: Filled missing ages with Median Age per Class.")

# 06. Oldest Surviving Passenger
oldest_survivor = df[df['Survived'] == 1].sort_values('Age', ascending=False).iloc[0]
print(f"\n06. Oldest Surviving Passenger:\n    - Name: {oldest_survivor['Name']}\n    - Age: {oldest_survivor['Age']}\n    - Class: {oldest_survivor['Pclass']}")

# 07. Gender Survival Rate
gender_survival = df.groupby('Sex')['Survived'].mean() * 100
print(f"\n07. Gender Survival Rate:\n{gender_survival}")

# 08. AgeGroup Binning
def get_age_group(age):
  if age < 18: return 'Child'
  elif age <= 60: return 'Adult'
  else: return 'Senior'

df['AgeGroup'] = df['Age'].apply(get_age_group)
age_group_survival = df.groupby('AgeGroup')['Survived'].mean() * 100
print(f"\n08. Survival Rate by Age Group:\n{age_group_survival}")

# 09. 3rd Class Gender Survival
class3_gender = df[df['Pclass'] == 3].groupby('Sex')['Survived'].mean() * 100
print(f"\n09. 3rd Class Gender Survival Rate:\n{class3_gender}")

# 10. Drop Cabin Data
df_cleaned = df.dropna(subset=['Cabin'])
remaining_rows = len(df_cleaned)
keep_pct = (remaining_rows / original_row_count) * 100
print(f"\n10. Dropping Missing Cabin Data:\n    - Rows remaining: {remaining_rows}\n    - Data retained: {keep_pct:.2f}%")