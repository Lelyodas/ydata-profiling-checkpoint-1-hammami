import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv('diabetes (1).csv')

print(df.head())
df.info()

missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)
zeros = (df == 0).sum()
print("Zeros in the dataset:\n", zeros)
summary_stats = df.describe()
print(summary_stats)

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("diabetes_report.html")

