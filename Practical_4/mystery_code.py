# What does this piece of code do?
# Answer:
# the total amount (sum) of 11 times random integer

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#define variable: total_rand，with the value 0
total_rand = 0

#define variable: progress, with the value 0
progress=0

#while loop: every time progress+1, take a random n and add it to total _rand 
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

#sum of 11 times 
print(total_rand)

