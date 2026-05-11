import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import the .csv file
os.chdir("/Users/juanxincai/IBI/IBI1_2025-26/Practical_10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#showing the third and fourth columns (the year and the DALYs) for the first 10 rows (inclusive)
print(dalys_data.iloc[0:10,2:4])

#maximum DALYs in Afghanistan for the first 10 years
afghanistan_data = dalys_data[dalys_data["Entity"] == "Afghanistan"].iloc[0:10]
max_dalys_year = afghanistan_data.loc[afghanistan_data["DALYs"].idxmax(), "Year"]
print(f"highest_DALYs_year：{max_dalys_year}")
#Comments: Across the first 10 years recorded for Afghanistan, the maximum DALYs value occurred in 1990

#Years recorded in Zimbabwe
new_entity = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[new_entity,"Year"]
first_year = zimbabwe_years.min()
last_year = zimbabwe_years.max()
print(f"All_years: {zimbabwe_years.values}")
print(f"starts at {first_year}, ends at {last_year}")
#Comments: the recording starts at 1990 and ends at 2019

#DALYs in 2019
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_country = recent_data.loc[recent_data["DALYs"].idxmax(), "Entity"]
min_country = recent_data.loc[recent_data["DALYs"].idxmin(), "Entity"]
print(f"the country which has the maximum DALYs in 2019 is {max_country}")
print(f"the country which has the mimumum DALYs in 2019 is {min_country}")
#Comments:the country which has the maximum DALYs in 2019 is Lesotho
#Comments:the country which has the mimumum DALYs in 2019 is Singapore

#for the country who has max DALYs in 2019 (Lesotho), the DALYs rate over time 
max_country_df = dalys_data.loc[dalys_data["Entity"] == max_country]
plt.plot(max_country_df.Year, max_country_df.DALYs, 'b-o')
plt.xticks(max_country_df.Year, rotation=-90)
plt.title("DALYs for the country who has the maximum DALYs in 2019 (Lesotho) Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.savefig("DALYs_in_max_country(Lesotho)_Over_Time.jpg")
plt.show()

#Asking one another question: How has the relationship between the DALYs in China and the UK changed over time? Are they becoming more similar, less similar?
# Filter data for China and United Kingdom
china = dalys_data.loc[dalys_data["Entity"] == "China"]
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom"]

# Create a plot comparing DALYs trends between China and UK over time
plt.figure(figsize=(12, 6))
plt.plot(china["Year"], china["DALYs"], "b-o", label="China", linewidth=2)
plt.plot(uk["Year"], uk["DALYs"], "r--s", label="United Kingdom", linewidth=2)

# Add labels and title
plt.title("DALYs Trends: China vs United Kingdom (1990–2019)")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.xticks(china["Year"], rotation=-90)
plt.legend()
plt.grid(alpha=0.3)

# Save and display the figure
plt.savefig("DALYs_China_UK_Comparison.jpg", dpi=300)
plt.show()

# Calculate the difference between China and UK DALYs values
differences = china["DALYs"].values - uk["DALYs"].values
print("Yearly DALYs Difference (China - UK):")
print(differences)

# Print conclusion
print("\nConclusion: The gap between China and UK is decreasing over time.")
print("They are becoming MORE similar.")
