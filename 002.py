fibo = [1, 2]
while fibo[-1] + fibo[-2] < 4000000:
    fibo.append(fibo[-1] + fibo[-2])

print sum(i for i in fibo if i % 2 == 0)
