import math

class Prime():

    def __init__(self, p: int) -> None:
        self.p = p
        self.prime = self.check_prime()

    #check whether a number is prime
    def check_prime(self) -> bool:
        for divisor in range(2, math.floor(math.sqrt(self.p))+1):
            if self.p % divisor == 0:
                return False
        return True

    # return the order of a mod p
    def order_a_mod_p(self, a: int) -> int:
        if a % self.p == 0:
            return 0
        k = 1
        while k < self.p - 1:
            if (a**k) % self.p == 1:
                return k
            else: 
                k += 1
        return k

    # return True if a is a primitive root mod p, False if not
    def check_primitive_root(self, a: int) -> bool:
        if self.order_a_mod_p(a) < (self.p - 1):
            return False
        return True
