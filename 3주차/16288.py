import sys

N, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
queue = [0 for i in range(K)]
isWrong = True

# 1. 부분 집합으로 나누기
# 2. 부분 집합의 가장 마지막 사람이랑 비교해서 더 큰 번호이면 해당 집합에 들어가기
# 3. 만약 모든 부분 집합에 들어갈 수 없다면 "NO" 출력
for i in range(N):
    isWrong = True
    for j in range(K):
        if(queue[j] < data[i]):
            queue[j] = data[i]
            isWrong = False
            break
    if(isWrong): break

if(isWrong): print("NO")
else: print("YES")
