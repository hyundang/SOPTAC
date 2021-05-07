import sys

T = int(sys.stdin.readline())
tc = [[] for i in range(T)]
res = []
for i in range(T):
    N = int(sys.stdin.readline())
    for j in range(N):
        score, rank = map(int, sys.stdin.readline().split())
        tc[i].append((score, rank))
    
    # 판별
    tc[i].sort()
    num = 1
    pivot = tc[i][0][1]
    for j in range(1, N):
        if(pivot > tc[i][j][1]):
            num += 1
            pivot = tc[i][j][1]
    res.append(num)

print('\n'.join(list(map(str,res))))

