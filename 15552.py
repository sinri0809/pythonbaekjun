import sys
#  입력 받기
T = int(input())
a = []
for val in range(T):
    a.append(list(map(int, sys.stdin.readline().split())))
    
for val in a:
    print(val[0]+val[1])
    # print(val)
