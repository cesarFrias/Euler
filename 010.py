from math import sqrt
sum_primes = 2
num = 2
num_primes = 1

def is_prime(num):
    return not any(num % x == 0 for x in range(2, int(sqrt(num)+1)))

while num < 2000000:
    num += 1
    if num % 2 != 0 and is_prime(num):
        sum_primes += num
        num_primes += 1
print sum_primes
