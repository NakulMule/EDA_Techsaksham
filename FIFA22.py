import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("FIFA22_PlayerCards.csv")
print(df.isnull().sum())
Drop columns with excessive missing values (Goalkeeper-specific stats for non-GKs)
df = df.drop(columns=['DIV', 'POS', 'HAN', 'REF', 'KIC', 'SPD'])

df.fillna(df.select_dtypes(include=[np.number]).median(), inplace=True)


for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

def bar_plot(variable):
    var = df[variable]
    varValue = var.value_counts()
    plt.figure(figsize=(9, 3))
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values, rotation=90)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print(f"{variable}: \n{varValue}\n")


print("Columns in dataset:", df.columns.tolist())


columns_plot = ['Position', 'Nationality', 'Weak Foot', 'Skill Moves', 'Preferred Foot']
for col in columns_plot:
    if col in df.columns:
        bar_plot(col)
    else:
        print(f"Column '{col}' not found in dataset.")


plt.figure(figsize=(12, 6))
sns.histplot(df['OVR'], bins=30, kde=True, color='blue')
plt.title('Distribution of Overall Ratings')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x=df['Position'], y=df['OVR'], hue=df['Position'], palette='coolwarm')
plt.xticks(rotation=90)
plt.title('Overall Rating by Player Position')
plt.legend([], [], frameon=False) 
plt.show()


plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()


plt.figure(figsize=(12, 6))
sns.scatterplot(x=df['PAC'], y=df['OVR'], hue=df['Position'], palette='viridis')
plt.title('Pace vs Overall Rating')
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x=df['SHO'], y=df['OVR'], hue=df['Position'], palette='coolwarm')
plt.title('Shooting vs Overall Rating')
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x=df['PAS'], y=df['OVR'], hue=df['Position'], palette='magma')
plt.title('Passing vs Overall Rating')
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x=df['DRI'], y=df['OVR'], hue=df['Position'], palette='plasma')
plt.title('Dribbling vs Overall Rating')
plt.show()
