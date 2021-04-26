import sys
from collections import deque

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

res = deque()

card_num = 1
for i in range(N):
    if(data[N-1-i] == 1):
        res.appendleft(card_num)
    elif(data[N-1-i] == 2):
        a = res.popleft()
        res.appendleft(card_num)
        res.appendleft(a)
    else:
        res.append(card_num)
    card_num = card_num + 1

for i in res:
    print(i, end=' ')