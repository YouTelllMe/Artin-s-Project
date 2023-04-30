import data_collect
import generate_data
import os
from integer import Integer

RANGEA = 100
RANGEP = 100000
# primes = [x for x in range(2, RANGEP+1) if Integer(x).prime]
primes = [x for x in range(900000, 900000+RANGEP+1) if Integer(x).prime]

# collects raw data
data_collect.data_collect(RANGEA, primes)

# generates in intended format
# generate_data.generate_data(primes)



