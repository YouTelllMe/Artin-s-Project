import pandas as pd
from integer import Integer
import os


#not used
def generate_data(primes):
    orda = pd.read_csv("order.csv")
    p1 = pd.read_csv("p1.csv")
    omega_orda = pd.read_csv("small_omega_orda.csv")
    Omega_orda = pd.read_csv("big_omega_orda.csv")
    omega_p1 = pd.read_csv("small_omega_p1.csv")
    Omega_p1 = pd.read_csv("big_omega_p1.csv")
    
    ratio_1 = Omega_p1 - Omega_orda
    ratio_3 = omega_p1.subtract(omega_orda)










