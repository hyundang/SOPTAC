import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

combis = []
for i in range(N):
    combi = list(map(list, combinations(data, i+1)))
    combis = combis + combi

res = 0
for i in combis:
    if(sum(i) == S):
        res = res + 1

print(res)
    