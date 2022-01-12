''' In this programe we aim to find the largest palindrome made from the product of two 3-digit numbers '''
''' Euler Project 4 '''

from typing import Sized

''' Function that checks if the input number is palindrome or not. '''
def is_palindrome(input):
    reversed_num = str(input)[::-1]
    str_input = str(input)
    result = True
    for i in range(len(str_input)):
            if str_input[i] != reversed_num[i]:
                result = False
                break
    return result

def find_num():
    list = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            var = i*j
            if is_palindrome(var):
                list.append(var)
                break
    list.sort()
    print(list[-1])


find_num()
