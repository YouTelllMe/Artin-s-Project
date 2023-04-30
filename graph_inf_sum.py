from integer import Integer
import matplotlib.pyplot as plt

RANGEP = 10000
primes = [x for x in range(2, RANGEP + 1) if Integer(x).prime]
prod = {2: 1}

def get_sum(prime):
    if prime in prod.keys():
        return prod[prime]
    else: 
        prod[prime] = 1/(prime*(prime-1)-1) + get_sum(primes[primes.index(prime)-1])
        return prod[prime]

if __name__ == "__main__":
    data = [get_sum(x) for x in primes]
    print(len(data))
    print(prod[primes[-1]])
    plt.plot(primes, data)
    plt.show()

