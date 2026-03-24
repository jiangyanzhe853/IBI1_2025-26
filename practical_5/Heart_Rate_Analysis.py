#input the data to create the list
L = (72,90,126,85,90,59,76,131,88,121,64)
num_patients = len(L)
mean_hr = sum(L) / num_patients
print(f"There are {num_patients} patients in the dataset. The mean heart rate is {mean_hr:.2f} bpm.")

#to catagroize the data, we create three lists to contain three types of data
Low_list = []
Normal_list = []
High_list = []
for i in L:
    if i < 60:
        Low_list.append(i)
    elif 60 <= i < 120:
        Normal_list.append(i)
    else:
        High_list.append(i)
low_count = len(Low_list)
normal_count = len(Normal_list)
high_count = len(High_list)

#find out which category has the most people
category_counts = {"Low": low_count, "Normal": normal_count, "High": high_count}
max_category = max(category_counts, key=category_counts.get)
print(f"\nThe category with the largest number of patients is: {max_category}")

#draw the plot
import matplotlib.pyplot as plt
labels = ["Low", "Normal", "High"]
sizes = [low_count, normal_count, high_count]
colors = ["#ff9999", "#66b3ff", "#99ff99"]
explode = (0, 0.1, 0)  
plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Distribution of Resting Heart Rate Categories")
plt.axis('equal')  
plt.show()
