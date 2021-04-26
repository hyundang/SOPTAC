import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x,y))

res = []
for i in range(N):
    rank = 0
    for j in range(N):
        if(j == i): continue
        if(data[i][0] < data[j][0] and data[i][1] < data[j][1]):
            rank = rank + 1
    res.append(rank+1)

for i in res:
    print(i, end=' ')