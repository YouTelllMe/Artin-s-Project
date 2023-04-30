from integer import Integer
import matplotlib.pyplot as plt
import math

ERROR = 0.000001
NUMPRIMES = math.ceil((-((1-math.sqrt(5))/2)*math.e**(-ERROR * math.sqrt(5))+(1+math.sqrt(5))/2)/(1-math.e**(-ERROR * math.sqrt(5))))
RANGEP = 10 * NUMPRIMES
primes = [x for x in range(2, RANGEP + 1) if Integer(x).prime]
prod = {2: 0.5}

def get_prod(prime):
    if prime in prod.keys():
        return prod[prime]
    else: 
        prod[prime] = (1-1/(prime*(prime-1))) * get_prod(primes[primes.index(prime)-1])
        return prod[prime]


if __name__ == "__main__":
    data = [get_prod(x) for x in primes]
    print(NUMPRIMES)
    print(len(data))
    print(prod[primes[-1]])
    plt.plot(primes, data)
    plt.show()

