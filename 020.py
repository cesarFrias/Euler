fat = 1
for i in xrange(1, 101):
    fat *= i

print sum(int(i) for i in fat.__str__())
