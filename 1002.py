import sys


t = int(input())
lst = []
for i in range(t):
    lst.append(list(map(int, sys.stdin.readline().split())))
    
for a in lst:
    xy = (a[3] - a[0])**2 + (a[4] - a[1])**2
    rp = (a[2] + a[5])**2
    rm = (a[2] - a[5])**2
    
    if rp > xy > rm:
        print(2)
    elif xy == rp or xy == rm != 0:
        print(1)
    # 동심원
    elif xy == rm == 0:
        print(-1)
    elif xy > rp or xy < rm:
        print(0)
    else:
        print(-1)
    

