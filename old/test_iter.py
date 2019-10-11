#!/usr/bin/python
import itertools

total = 123
groups = 6

result = [0 for i in range(groups)]
indices = range(groups)

index = itertools.cycle(indices)
for i in range(total):
    result[index.next()] += 1
    i += 1
print result
