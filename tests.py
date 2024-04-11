from functions import *
# This code defines several functions for testing a Binary Decision Diagram (BDD)
# and validating it using the given parameters.

def test_BDD(prime, temp):
    # Validates the Binary Decision Diagram (BDD) using the given parameters.
    for i in range(0, 32):
        for j in range(0, 32):
            if test_prime(prime, i) == 0:
                continue
            else:
                if (test_even(j) & test_bdd(temp, i, j)) == 0 & j == 31:
                    return False
    return True

def test_bdd(bdd, temp_1, temp_2):
    # Tests the BDD with the given inputs and returns the result.
    if ("And(" + (bool_var_test(temp_1, 'xx')) + ", " + (bool_var_test(temp_2, 'yy')) + ")") in str(bdd2expr(bdd)):
        return 1
    else:
        return 0

def test_even(num):
    # Checks if a number is even and returns the result.
    if (num % 2) == 0:
        return 1
    else:
        return 0

def test_prime(bdd, num):
    # Checks if a number is prime using the BDD and returns the result.
    temp = "And(" + bool_var_test(num, 'yy') + ")"
    
    if temp in str(bdd2expr(bdd)):
        return 1
    else:
        temp2 = temp.replace(', yy4', '')
        if temp2 in str(bdd2expr(bdd)):
            return 1
        else:
            return 0

def bool_var_test(number, prefix):
    # Generates boolean variables for a given number and prefix.
    temp = []
    if prefix is None:
        prefix = 'xx'
        
    binary = format(number, '05b')
    
    for i, bit in enumerate(binary, start=1):
        if bit == '0':
            part = f"~{prefix}{i}"
        else:
            part = f"{prefix}{i}"
        
        temp.append(part)
    return ", ".join(temp)










