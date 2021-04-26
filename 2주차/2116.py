import sys

N = int(sys.stdin.readline())
dices = []
for i in range(N):
    dice = list(map(int, sys.stdin.readline().split()))
    dices.append(dice)

results = []
for i in range(6):
    num = dices[0][i]
    if(i==0):
        a=dices[0][0]
        b=dices[0][5]
        dices[0].remove(a)
        dices[0].remove(b)
        result = max(dices[0])
        dices[0].insert(0, a)
        dices[0].insert(5, b)
    elif(i==1):
        a=dices[0][1]
        b=dices[0][3]
        dices[0].remove(a)
        dices[0].remove(b)
        result = max(dices[0])
        dices[0].insert(1, a)
        dices[0].insert(3, b)
    elif(i==2):
        a=dices[0][2]
        b=dices[0][4]
        dices[0].remove(a)
        dices[0].remove(b)
        result = max(dices[0])
        dices[0].insert(2, a)
        dices[0].insert(4, b)
    elif(i==3):
        a=dices[0][1]
        b=dices[0][3]
        dices[0].remove(a)
        dices[0].remove(b)
        result = max(dices[0])
        dices[0].insert(1, a)
        dices[0].insert(3, b)
    elif(i==4):
        a=dices[0][2]
        b=dices[0][4]
        dices[0].remove(a)
        dices[0].remove(b)
        result = max(dices[0])
        dices[0].insert(2, a)
        dices[0].insert(4, b)
    else:
        a=dices[0][0]
        b=dices[0][5]
        dices[0].remove(a)
        dices[0].remove(b)
        result = max(dices[0])
        dices[0].insert(0, a)
        dices[0].insert(5, b)
    

    for j in range(1, N):
        idx = dices[j].index(num)
        if(idx==0): 
            a = num
            b = dices[j][5]
            num = dices[j][5]
            dices[j].remove(a)
            dices[j].remove(b)
            result = result + max(dices[j])
            dices[j].insert(0, a)
            dices[j].insert(5, b)
        elif(idx==1):
            a = num
            b = dices[j][3]
            num = dices[j][3]
            dices[j].remove(a)
            dices[j].remove(b)
            result = result + max(dices[j])
            dices[j].insert(1, a)
            dices[j].insert(3, b)
        elif(idx==2):
            a = num
            b = dices[j][4]
            num = dices[j][4]
            dices[j].remove(a)
            dices[j].remove(b)
            result = result + max(dices[j])
            dices[j].insert(2, a)
            dices[j].insert(4, b)
        elif(idx==3):
            a = num
            b = dices[j][1]
            num = dices[j][1]
            dices[j].remove(a)
            dices[j].remove(b)
            result = result + max(dices[j])
            dices[j].insert(1, b)
            dices[j].insert(3, a)
        elif(idx==4):
            a = num
            b = dices[j][2]
            num = dices[j][2]
            dices[j].remove(a)
            dices[j].remove(b)
            result = result + max(dices[j])
            dices[j].insert(2, b)
            dices[j].insert(4, a)
        else:
            a = num
            b = dices[j][0]
            num = dices[j][0]
            dices[j].remove(a)
            dices[j].remove(b)
            result = result + max(dices[j])
            dices[j].insert(0, b)
            dices[j].insert(5, a)
    results.append(result)


print(max(results))