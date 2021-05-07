import sys
    
N = int(sys.stdin.readline())

# 가능한 경우의 수 
result = 0
a_row = [0]*(N+1)

def DFS(row, N):
    global a_row
    if(row > N):
        global result
        result += 1
    else:
        for i in range(N):
            a_row[row] = i+1
            if(isOkay(row, i+1)):
                DFS(row+1, N)
            else:
                a_row[row] = 0

# 백트래킹 과정
def isOkay(row, col):
    global a_row
    for i in range(1, row):
        # 위
        if(a_row[i] == col):
            return False
        # 대각선
        if(abs(a_row[row]-a_row[i]) == abs(row-i)):
            return False
    return True

# dfs 수행
DFS(1, N)

print(result)