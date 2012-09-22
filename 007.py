num = 2
num_primes = 1
stop_in = 10001

def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    return not any(num % x == 0 for x in range(2, int(num**0.5)+1))

while num_primes < stop_in:
    num += 1
    if is_prime(num):
        num_primes += 1
print num
