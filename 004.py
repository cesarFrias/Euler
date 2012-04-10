# -*- coding: utf-8 -*-


MIN_NUMBER = 99
num_a = 999
num_b = 999
palindromes = []

def is_palindrome(number):
    """Returns True if a number is palindrome"""
    return number.__str__() == number.__str__()[::-1]

while num_a > MIN_NUMBER:
    mult = num_a * num_b
    if is_palindrome(mult):
        palindromes.append(mult)
    num_b = num_b - 1
    if num_b == MIN_NUMBER:
        num_a = num_a - 1
        num_b = num_a
palindromes.sort()
print palindromes[-1]
