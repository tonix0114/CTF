from z3 import *

s = Solver()
arr = [BitVec('a%i' %i, 32) for i in range(9)]
for i in range(9):
    s.add(Or(And(arr[i] >= ord('a'), arr[i] <= ord('z')) , arr[i] == ord('_')))
k1 = 1
k2 = 0
for i in range(9):
    k1 = (arr[i] + k1)
    k2 = k1 + k2

s.add((k1 ^ k2) == 0x12e1)
if(s.check() == sat):
    m = s.model()
    flag = ''.join(map(lambda x: chr(m[x].as_long()), arr))
    print(flag)
