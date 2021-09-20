import sys


n = int(input())
number_lst = [int(sys.stdin.readline()) for _ in range(n)]

number_lst.sort()
for i in number_lst:
    print(i)
