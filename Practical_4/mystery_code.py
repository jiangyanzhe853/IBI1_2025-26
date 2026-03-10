# What does this piece of code do?
# Answer:
# the total amount of 11 times random integer

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#定义变量total_rand，赋值为0
total_rand = 0

#定义变量progress，赋值为0
progress=0

#while loop
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

#11次取随机数之和
print(total_rand)

