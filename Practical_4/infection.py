#create varible i for the studnets who are infected
i = 5

#create varible day for the total days
day = 0

#while loop: every day increase 40% infected students, increase one day until all students infected
while i <=91:
    day +=1
    print(i)
    i=int(1.4*i)
print("all infected")
print(f"infect all students need{day}days")