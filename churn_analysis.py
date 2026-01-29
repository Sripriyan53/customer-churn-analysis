import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print("Total Customers:")
print(len(df))

print("\nChurn Count:")
print(df['Churn'].value_counts())

print("\nChurn by Contract Type:")
print(df.groupby('Contract')['Churn'].value_counts())
