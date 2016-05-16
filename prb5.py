from math import sqrt

num = 1
primes = []
check = []

def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(math.sqrt(n))+1)
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1            
    return primes

print factorize(int(sys.argv[1]))		


