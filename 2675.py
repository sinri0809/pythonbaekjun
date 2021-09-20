import sys


T = int(input())
lst = []
for temp in range(T):
    lst.append(list(map(str, sys.stdin.readline().split(' '))))
    
for lst in lst:
    numb = int(lst[0])
    str1 = lst[1].rstrip()
    for c in str1:
        print("{}".format(c) * numb, end="")
    
    print()
