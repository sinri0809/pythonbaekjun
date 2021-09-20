import sys


n = int(input())
count_arr = [0 for _ in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    count_arr[num] += 1
    
for i in range(10001):
    if count_arr[i] != 0:
        print('{0}\n'.format(i)*count_arr[i], end='')
