import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

heapq.heapify(data)

for i in range(m):
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    heapq.heappush(data, a+b)
    heapq.heappush(data, a+b)

print(sum(data))


