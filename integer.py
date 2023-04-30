import math

class Integer():

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
            if (self.p - 1) % k == 0 and (Integer.exp_by_squaring(a,k, self.p) % self.p) == 1:
                return k
            else: 
                k += 1
        return k

    # return True if a is a primitive root mod p, False if not
    def check_primitive_root(self, a: int) -> bool:
        if self.order_a_mod_p(a) < (self.p - 1):
            return False
        return True

#     @staticmethod
#     def exp_by_squaring(a: int, k: int) -> int:
#         if k == 0:
#             return 1
#         elif k % 2 == 0:
#             return Integer.exp_by_squaring(a**2, k/2)
#         else:
#             return a * Integer.exp_by_squaring(a, k-1)

    # suggested by Greg Martin
    @staticmethod
    def exp_by_squaring(a: int, k: int, p: int) -> int:
        if k == 0:
            return 1
        elif k % 2 == 0:
            return Integer.exp_by_squaring(a**2 % p, k/2, p)
        else:
            return (a * Integer.exp_by_squaring(a, k-1, p)) % p

    @staticmethod
    def prime_factorize(num):
        factors = {}
        for integer in range(2, num+1):
            if num == 1:
                break
            elif Integer(integer).prime:
                while num % integer == 0:
                    try:
                        factors[integer] += 1
                    except KeyError:
                        factors[integer] = 1
                    finally:
                        num /= integer
        return factors
        
    def get_Omega(self, a: int, order: int = None) -> int:
        total_multiplicity = 0
        if order == None:
            factor_multiplicity = Integer.prime_factorize(a).values()
        else: 
            factor_multiplicity = Integer.prime_factorize(order).values()
        for multiplicity in factor_multiplicity:
            total_multiplicity += multiplicity
        return total_multiplicity

    def get_omega(self, a: int, order: int = None) -> int:
        if order == None:
            return len(Integer.prime_factorize(a))
        return len(Integer.prime_factorize(order))
