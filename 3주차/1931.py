import sys

# 입력값
N = int(sys.stdin.readline())
data = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    data.append((start, end))

# 데이터 정렬
data.sort(key=lambda x : (x[1], x[0]))
start = data[0][0]
end = data[0][1]

# 그리디 알고리즘: 가장 빨리 끝나는 회의 찾기
i = 1
res = 1
while(i < N):
    if(data[i][0] >= end):
        start = data[i][0]
        end = data[i][1]
        res += 1
    i += 1

print(res)