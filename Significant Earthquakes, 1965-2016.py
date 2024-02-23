import pandas as pd
import matplotlib
matplotlib.use('TkAgg') # or 'Qt5Agg'
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('database.csv')
# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
# View 1: Scatter plot of Magnitude vs. Depth
axs[0, 0].scatter(df['Magnitude'], df['Depth'], s=10, alpha=0.5)
axs[0, 0].set_xlabel('Magnitude')
axs[0, 0].set_ylabel('Depth (km)')
axs[0, 0].set_title('Magnitude vs. Depth of Earthquakes')
axs[0, 0].grid(True)
# View 2: Histogram of Earthquake Magnitudes
axs[0, 1].hist(df['Magnitude'], bins=20, edgecolor='black')
axs[0, 1].set_xlabel('Magnitude')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Distribution of Earthquake Magnitudes')
axs[0, 1].grid(True)
# View 3: Bar plot of Earthquake Types
earthquake_types = df['Type'].value_counts()
axs[1, 0].bar(earthquake_types.index, earthquake_types.values)
axs[1, 0].set_xlabel('Earthquake Type')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Types of Earthquakes')
axs[1, 0].grid(True)
plt.xticks(rotation=45)
# View 4: Violin plot of Earthquake Depths
axs[1, 1].violinplot(df['Depth'], vert=False, showmedians=True)
axs[1, 1].set_xlabel('Depth (km)')
axs[1, 1].set_title('Distribution of Earthquake Depths')
# Adjust layout and display the plots
plt.tight_layout()
plt.show()