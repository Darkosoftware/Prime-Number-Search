import math
import numpy as np

#Search for prime numbers

print("Hi there, Let me help you find some primes, input a number value")

n = int(input("Pick your number: "))

def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n > 2 and n % 2 == 0:
		return False
	for i in range(3,n):
		if n % i == 0:
			return False
	return True

print(is_prime(n))

print("Now we can try finding all primes in a range!")
n_min = int(input("Pick the start of the range: "))
n_max = int(input("Pick the end of the range: "))

def get_primes(n_min, n_max):
	result = []
	for x in range(max(n_min, 2), n_max):
		has_factor = False
		for y in range(2, int(np.sqrt(x)) + 1):
			if x % y == 0:
				has_factor = True
				break
		if not has_factor:
			result.append(x)
	return result

print(get_primes(n_min, n_max))

input("Press enter to close.")

#program works perfectly in IDE but wont open if you click directly. 
