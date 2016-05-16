from math import sqrt

def fibonacci(num):
	summation = 0
	for i in range(1,num):
		f = ((1+sqrt(5))**i - (1-sqrt(5))**i)/((2**i)*sqrt(5))
		print f
		if f > num:
			break
		if int(f) % 2 == 0:
			summation = summation + f

	return summation

total = fibonacci(4000000)
print total
