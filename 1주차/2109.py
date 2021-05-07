import sys

N = int(sys.stdin.readline())
if(N == 0):
    print(0)
else:
    data = []
    for i in range(N):
        p, d = map(int, sys.stdin.readline().split())
        data.append([-p, d, True])

    data.sort(key=lambda x : x[1], reverse=True)
    maxDate = data[0][1]
    data.sort(key=lambda x : (x[0], x[1]))

    # 가능한 강연 검사
    sum = 0
    while(maxDate > 0):
        for i in range(N):
            if(data[i][1] >= maxDate and data[i][2]):
                sum -= data[i][0]
                data[i][2] = False
                break
        maxDate -= 1

    print(sum)