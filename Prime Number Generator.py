#Import Libaries

import time

Primes = input("Please Enter how many numbers you would like to check are prime, starting from 2 to anything!: ")
Message = ("Ok - Let me calculate all prime numbers from 2 to %s. Give me a few seconds....i'm slow!")
print(Message %(Primes))
time.sleep (5)
for i in range (2,int(Primes)+1):
	j = 2
	counter = 0
	while j < i:
		if i % j == 0:
				counter = 1
				j = j + 1
		else: 	
				j = j + 1
	if counter == 0:
		print(str(i) + " is a prime number")
	else:
		counter = 0
