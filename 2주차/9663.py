# 시간초과 해결해야 함
import sys
    
N = int(sys.stdin.readline())


# 가능한 경우의 수
global result   
result = 0

def DFS(row, a_row):
    if(row > N):
        global result
        result = result + 1
    else:
        for i in range(N):
            a_row[row] = i+1
            if(isOkay(row, i+1, a_row)):
                DFS(row+1, a_row)
            else:
                a_row[row] = 0


def isOkay(row, col, a_row):
    for i in range(1, row):
        # 위
        if(a_row[i] == col):
            return False

        # 대각선
        if(abs(a_row[row]-a_row[i]) == abs(row-i)):
            return False
        
    return True

# dfs 수행: (1,1) -> (1,N)까지 반복
for i in range(N):
    a_row = [0]*(N+1)
    a_row[1] = i+1

    DFS(2, a_row)

print(result)