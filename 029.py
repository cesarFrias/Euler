# -*- coding: utf-8 -*-
MIN = 2
MAX = 101
a = 2
b = 2
nums = set()

for a in xrange(MIN, MAX):
    for b in xrange(MIN, MAX):
        nums.add(a ** b)
    b = 2

print len(nums)
