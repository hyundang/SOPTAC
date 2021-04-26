import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

res = [-1 for i in range(N)]
for i in range(1, N):
    idx = i-1
    x = data[idx]
    while(x < data[i]):
        idx = res[idx]
        x = data[idx]
        if(idx == -1): break;
    res[i] = idx

for i in res:
    print(i+1, end=' ')
