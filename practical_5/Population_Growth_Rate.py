import matplotlib.pyplot as plt

#create a year dictionary inside the country dictionary 
population_data = {
    "UK": {"2020": 66.7, "2024": 69.2},
    "China": {"2020": 1426, "2024": 1410},
    "Italy": {"2020": 59.4, "2024": 58.9},
    "Brazil": {"2020": 208.6, "2024": 212.0},
    "USA": {"2020": 331.6, "2024": 340.1}
}

#use the data to caculate the change rate
percent_changes = {}
for country, data in population_data.items():
    pop_2020 = data["2020"]
    pop_2024 = data["2024"]
    pct_change = ((pop_2024 - pop_2020) / pop_2020) * 100
    percent_changes[country] = round(pct_change, 2)


#A printed list	of population changes sorted from largest increase to largest decrease and a statement of the countries	with the largest increase and largest decrease
sorted_changes = sorted(percent_changes.items(), key=lambda x: x[1], reverse=True)
print("\nPopulation changes in descending order:")
for country, change in sorted_changes:
    print(f"- {country}: {change}%")

max_increase_country = sorted_changes[0][0]
max_increase_value = sorted_changes[0][1]
max_decrease_country = sorted_changes[-1][0]
max_decrease_value = sorted_changes[-1][1]
print(f"\nLargest increase: {max_increase_country} ({max_increase_value}%)")
print(f"Largest decrease: {max_decrease_country} ({max_decrease_value}%)")

countries = list(percent_changes.keys())
changes = list(percent_changes.values())

#draw the plot
plt.figure(figsize=(8, 5))
bars = plt.bar(countries, changes, color=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd'])

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}%', ha='center', va='bottom')

plt.xlabel('Country')
plt.ylabel('Population Percentage Change (%)')
plt.title('Population Percentage Change (2020-2024)')
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)  
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
