import pandas as pd
from integer import Integer
import os
import time

CURRENT = os.getcwd()
PATH = os.path.join(CURRENT, "data")
if not os.path.isdir(PATH):
    os.mkdir(PATH)
os.chdir(PATH)

def data_collect(RANGEA, primes):
    #set range, set up for data structure
    order = {}
    primitive_root = {}
    omega = {'orda':{}, 'p1':{}}
    Omega = {'orda':{}, 'p1':{}}
    ratio_1 = {}
    ratio_2 = {}
    ratio_3 = {}

    start_time = time.time()
    for a in list(range(-RANGEA, -1)) + list(range(2, RANGEA + 1)):
        #initiate lists to append to 
        order[a] = []
        primitive_root[a] = []
        omega["orda"][a] = []
        Omega["orda"][a] = []
        omega["p1"][a] = []
        Omega["p1"][a] = []
        ratio_1[a] = []
        ratio_2[a] = []
        ratio_3[a] = []

        # obtain and append the values for each p
        for p in primes:
            print("Computing data for a ="+str(a)+ " p =" + str(p))
            
            start_order = time.time()
            prime = Integer(p)
            orda = prime.order_a_mod_p(a)
            end_order = time.time()
            print("Order: "+ str(end_order-start_order)+" seconds")
            
            pr = (orda == p-1)
            order[a].append(orda)
            primitive_root[a].append(pr)
                  
            start_omega = time.time()
            omega_p1 = prime.get_omega(p-1)
            end_omega = time.time()
            print("omega: "+ str(end_omega-start_omega)+" seconds")

            start_Omega = time.time()
            Omega_p1 = prime.get_Omega(p-1)
            end_Omega = time.time()  
            print("Omega: "+ str(end_Omega-start_Omega)+" seconds")
            
            if orda == 0:
                omega["orda"][a].append(float("inf"))
                Omega["orda"][a].append(float("inf"))
                ratio_1[a].append(float("inf"))
                ratio_2[a].append(float("inf"))
                ratio_3[a].append(float("inf"))
            else: 
                omega_orda = prime.get_omega(a, orda)
                Omega_orda = prime.get_Omega(a, orda)
                omega_p1 = prime.get_omega(p-1)
                Omega_p1 = prime.get_Omega(p-1)
                omega["orda"][a].append(omega_orda)
                Omega["orda"][a].append(Omega_orda)
                ratio_1[a].append(Omega_p1-Omega_orda)
                ratio_2[a].append(prime.get_omega((p-1)//orda))
                ratio_3[a].append(omega_p1-omega_orda)
            omega["p1"][a].append(omega_p1)
            Omega["p1"][a].append(Omega_p1)

    #import data to pandas dataframes, then save to csv
    df_order = pd.DataFrame(data=order, index=primes)
    df_prim_root = pd.DataFrame(data=primitive_root, index=primes)
    df_omega_orda = pd.DataFrame(data=omega["orda"], index=primes)
    df_Omega_orda = pd.DataFrame(data=Omega["orda"], index=primes)
    df_omega_p1 = pd.DataFrame(data=omega["p1"], index=primes)
    df_Omega_p1 = pd.DataFrame(data=Omega["p1"], index=primes)
    df_ratio_1 = pd.DataFrame(data=ratio_1, index=primes)
    df_ratio_2 = pd.DataFrame(data=ratio_2, index=primes)
    df_ratio_3 = pd.DataFrame(data=ratio_3, index=primes)


    df_order.to_csv("order_new.csv")
    df_prim_root.to_csv("prim_root_new.csv")
    df_omega_orda.to_csv("small_omega_orda_new.csv")
    df_Omega_orda.to_csv("big_omega_orda_new.csv")
    df_omega_p1.to_csv("small_omega_p1_new.csv")
    df_Omega_p1.to_csv("big_omega_p1_new.csv")
    df_ratio_1.to_csv("ratio1_new.csv")
    df_ratio_2.to_csv("ratio2_new.csv")
    df_ratio_3.to_csv("ratio3_new.csv")
    end_time = time.time()
    print("Total Time: "+str(start_time-end_time+" seconds"))
