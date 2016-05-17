from math import factorial
count = 0

for n in range(1,100):
	for r in range(1,100):
		if r <= n:
			t = n-r
			value = factorial(n)/(factorial(r)*factorial(t))
			if value > 1000000:
				count = count + 1


print count
