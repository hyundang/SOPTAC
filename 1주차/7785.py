import sys

res = []

N = int(sys.stdin.readline())
for i in range(N):
    name, log = map(str, sys.stdin.readline().split())
    if(log == "enter"):
        res.append(name)
    else:
        res.remove(name)

res.sort(reverse=True)
for name in res:
    print(name)
