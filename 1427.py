import sys


n = int(sys.stdin.readline())
temp_lst = [i for i in str(n)]
print(''.join(str(i) for i in sorted(temp_lst, reverse=True)))
