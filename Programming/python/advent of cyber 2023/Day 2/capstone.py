import os.path
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(os.path.join(
    os.path.dirname(__file__), "network_trafic.csv"))

# print(df)
# print(df.head(5))

# print(df.count())

# Use Pandas to group the analyse the data in Source, Destination and Protocol.
# Apply functions such as sum, average, size and describe to this grouping.

print(df.groupby(['Source']).size().sort_values(ascending=False))

print()
# Group the columns "Department" and "Prize"
# Use describe to give a summary breakdown of the data in percentiles
# print(df.groupby(['Department'])['Prize'].describe())

print(df.groupby(['Protocol']).size().sort_values(ascending=False))
