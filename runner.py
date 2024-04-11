
# Runner Simply Runs the Given tests and functions to check the correctness of the code.
# It also visualizes the BDDs for the given expressions and edges.
from functions import *
from tests import *

prime_list = [3,5,7,11,13,17,19,23,29,31]
even_list = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

   
even = E_P_lists(even_list, 'xx')
prime = E_P_lists(prime_list, 'yy')

R = edges()
RR = BDD(R)                       #this is the Graph in BDD form for the given edges
RR2 = bad_apple(RR, RR)            #this is two step reachability graph
RR2X = closure(RR2)
EVEN_BDD = expr2bdd(expr(even))
PRIME_BDD = expr2bdd(expr(prime))
    
visualize_bdd(EVEN_BDD, 'even_bdd')
visualize_bdd(PRIME_BDD , 'prime_bdd')

#print(str(expr(prime))) this is just to check the expression of the prime numbers


print("RR(27, 3) is " + "{}".format(test_bdd(RR, 27, 3)))
print("RR(16, 20) is " + "{}".format(test_bdd(RR, 16, 20)))
print("EVEN(14) is " + "{}".format(test_even(14)))
print("EVEN(13) is " + "{}".format(test_even(13)))
print("PRIME(7) is " + "{}".format(test_prime(PRIME_BDD, 7)))
print("PRIME(2) is " + "{}".format(test_prime(PRIME_BDD, 2)))
print("RR2(27, 6) is " + "{}".format(test_bdd(RR2, 27, 6)))
print("RR2(27, 9) is " + "{}".format(test_bdd(RR2, 27, 9)))
print("The Statement for A is "+ "{}".format(test_BDD(PRIME_BDD, RR2X)))
    
    
    
    
    
