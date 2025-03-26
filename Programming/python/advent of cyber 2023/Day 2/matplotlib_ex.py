import os.path
import pandas as pd
import matplotlib.pyplot as plt

plt.xlabel('Months of the Year')
plt.ylabel('Number of Toys Produced')

plt.title(
    'A Line Graph Showing the Number of Toys Produced Between September and December')

plt.plot(['September', 'October', 'November', 'December'], [8, 14, 80, 160])
plt.show()


spreadsheet = pd.read_csv(os.path.join(
    os.path.dirname(__file__), 'drinks.csv'))

drinks = spreadsheet['Drink']
votes = spreadsheet['Vote']

print(spreadsheet)

# Here, we are going to tell pyplot the size of the figure. Find a value that improves readability
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

# plt.bar tells pyplot to use a bar graph. the `h` means horizontal, `v` can be used for a vertical bar graph.
plt.barh(drinks, votes, color='skyblue')

# Set the labels for the graph
plt.xlabel('Number of Votes')
plt.ylabel('Name of Drink')
plt.title('A Bar Graph Showing the Employees Favourite Drinks')

# Optional - invert the y-axis for better readability (most popular at the bottom)
plt.gca().invert_yaxis()

plt.show()
