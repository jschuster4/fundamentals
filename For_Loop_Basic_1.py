# Basic, print all integers from 0-150
for i in range(0, 151):
    print(i)

# Multiples of 5

for i in range(0, 1001, 5):
    print(i)

# Counting, the Dojo way
for i in range(0, 101, 1):
    if(i%5 == 0 and i%10 == 0 and i!= 0 ):
        print("Coding Dojo")
    elif(i%5 ==0 and i!=0):
        print("Coding")
    else: 
        print(i)

# whoa. That suckers huge
sum = 0
for i in range(1, 500000,2):
    sum = sum + i
print(sum)

# Countown by fours
for i in range (2018, 0, -4):
    print(i)

# Flexible Counter
lowNumber = 2
highNumber = 9
mult = 3
for i in range(lowNumber, highNumber + 1):
    if(i % mult == 0):
        print(i)