import sys

N, K = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
    a = int(sys.stdin.readline())
    data.append(a)

res = 0
data.sort(reverse=True)
for i in range(N):
    if(data[i] <= K):
        while(data[i] <= K):
            K -= data[i]
            res += 1
    if(K == 0): break

print(res)