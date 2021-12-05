from bisect import *
from collections import deque

l = [1,2,3,4,5,6,7,8,9]
print(bisect_left(l, 3))
print(bisect_right(l, 3))

l = deque([1,2,3])
l.append(1)
print(l)
print(l[0])
l.extend([2,3,4])
print(l)
l = l + l
print(l)