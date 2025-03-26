import os.path
import pandas as pd

data = [['Ben', 24, 'United Kingdom'],
        ['Jacob', 32, 'United States of America'],
        ['Alice', 19, 'Germany']]

df = pd.DataFrame(data, columns=['Name', 'Age', 'Country of Residence'])
print(df)
print(df.loc[1])

# Load awards.csv as a dataframe
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "awards.csv"))
print(df)

# Group the columns "Department" and "Prize"
# Use sum to return the sum of the values of each column
print(df.groupby(['Department'])['Prize'].sum())

# Group the columns "Department" and "Prize"
# Use describe to give a summary breakdown of the data in percentiles
print(df.groupby(['Department'])['Prize'].describe())
