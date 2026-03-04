#Program to check for prime numbers in a range
#Check for primes and store in an array
#To reduce number of computations, the numbers ending in 1,3,7,9 are checked
#Still a trial division method

#Sub program to check for primes

from math import sqrt
import csv
import time

def prime(n):
    for factor in range(3,int(sqrt(n)+1)):
        if (factor%10 == 1) or (factor%10 == 3) or (factor%10 == 7) or (factor%10 == 9):
            if n%factor == 0:
                return False
    return True

#Main program
#Designed to reduce computation for bigger numbers

t0 = time.time()
x = int(input('Enter the starting number: '))
y = int(input('Enter the starting number: '))
a = []      #Initializing the array to store primes
one = []
three = []
seven = []
nine = []

ones = 0        #Initializing the count for primes ending in 1
twos = 0        #Initializing the count for primes ending in 2
threes = 0      #Initializing the count for primes ending in 3
fives = 0       #Initializing the count for primes ending in 5
sevens = 0      #Initializing the count for primes ending in 7
nines = 0       #Initializing the count for primes ending in 9

#Sending the value to the function to check whether it is a prime number

if x > y:
    raise TypeError('Ending number should be greater than starting number')
else:
    for i in range(x,y+1):
        if i <= 5:
            if (i == 2) or (i == 3) or (i == 5):
                a.append(i)
        elif i > 5:
            if (i%10 == 1) or (i%10 == 3) or (i%10 == 7) or (i%10 == 9):    #Not sending numbers that are divisible by 2 or 5
                if prime(i):
                    a.append(i)

    #Sorting out numbers ending in ones, two, threes, fives, sevens and nines

    for j in range(len(a)):
        if a[j]%10 == 1:        #checking for primes ending with 1
            one.append(a[j])
            ones += 1
        elif a[j]%10 == 2:      #checking for primes ending with 2
            twos += 1
        elif a[j]%10 == 3:      #checking for primes ending with 3
            three.append(a[j])
            threes += 1
        elif a[j]%10 == 5:      #checking for primes ending with 5
            fives += 1
        elif a[j]%10 == 7:      #checking for primes ending with 7
            seven.append(a[j])
            sevens += 1
        elif a[j]%10 == 9:     #checking for primes ending with 9
            nine.append(a[j])
            nines += 1


#Printing results
print('Number of primes in this range are: ',len(a))
print('Number of primes ending in ones: ',len(one))
print('Number of primes ending in threes: ',len(three))
print('Number of primes ending in sevens: ',len(seven))
print('Number of primes ending in nines: ',len(nine))
t1 = time.time()
print('Total time taken: ',(t1-t0),'seconds')
