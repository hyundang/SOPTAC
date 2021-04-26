import sys
from itertools import combinations 

L, C = map(int, sys.stdin.readline().split())
chars = list(map(str, sys.stdin.readline().split()))

vowels = [] #모음
cons = [] #자음
for i in chars:
    if(i in "aeiou"): 
        vowels.append(i)
    else:
        cons.append(i)

res = []
a = 1 #모음 개수
b = L-a #자음 개수
while(a <= len(vowels) and b >= 2):
    v_items = list(map(list, combinations(vowels, a)))
    c_items = list(map(list, combinations(cons, b)))
    for i in v_items:
        for j in c_items:
            k = i + j
            k.sort()
            res.append("".join(k))
    a = a + 1
    b = L - a

# 결과값 출력
res.sort()
print('\n'.join(res))
