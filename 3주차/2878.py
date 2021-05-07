import sys

M, N = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

# 못받는 사탕의 개수를 분배하자!
total = sum(data)
sub = M - total

res = 0
for i in range(N):
    lack = min(data[i], sub//(N-i))
    res += lack**2
    sub -= lack

print(res)