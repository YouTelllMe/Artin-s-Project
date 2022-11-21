import pandas as pd
from prime import Prime

#set range, set up for data structure
RANGE = 1000
primes = [x for x in range(2, RANGE + 1) if Prime(x).prime]
order = {}
primitive_root = {}

#counter for prim roots vs total entries 
prim_root_counter = 0
total_enties = 0


for a in range(2, RANGE + 1):
    #initiate lists to append to 
    order[a] = []
    primitive_root[a] = []
    for p in primes:
        # calculate order and check if it's a prim root
        total_enties += 1
        orda = Prime(p).order_a_mod_p(a)
        pr = (orda == p-1)
        if pr:
            prim_root_counter+=1
        order[a].append(orda)
        primitive_root[a].append(pr)


#import data to pandas dataframes, then save to csv
df_order = pd.DataFrame(data=order, index=primes)
df_prim_root = pd.DataFrame(data=primitive_root, index=primes)
df_order.to_csv("order.csv")
df_prim_root.to_csv("prim_root.csv")

#print percentage of primitive roots
print(prim_root_counter / total_enties)