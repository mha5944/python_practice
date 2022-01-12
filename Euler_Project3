'''
    In this code the aim is to find the largest prime factor of a dsired number
'''

import numpy as np

num = 600851475143
prime = []

def is_prime(input):

    var = (input // 2) + 1
    result = True
    for j in range(2,var):
        if input%j == 0:
            result = False
            break

    return result
    
 ''' This function gives us an list of prime factors of the input number '''

def factors(input):

    var = (input // 2) + 1
    ident = 0
    for i in range(2,int(var)):
        if input%i == 0:
            ident = 1
            if is_prime(i):
                prime.append(i)
                factors(input/i)
                break
        if i+1 == int(var) and ident == 0:
            prime.append(input)
    return prime

''' Finding the largest prime factor of the input '''
def lpf(input):

    prime_list = factors(input)
    unique_list = np.unique(prime_list)
    print(unique_list)
    return prime_list[-1]

print(lpf(num))
