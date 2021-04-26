import heapq
import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    p, d = map(int, sys.stdin.readline().split())
    data.append((d, -p))

heapq.heapify(data)

sum = 0
day = 0
for i in range(N):
    item = heapq.heappop(data)
    if(item[0] > day):
        sum = sum - item[1]
        day = item[0]

print(sum)

#그리디 알고리즘 필요