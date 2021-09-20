# 1
# 2-7  =6
# 8-19   =12
# 20-37  =18

x = int(input())

N = ((x/3) - (1/12))**(1/2) + 0.5
# print(N)
n = int(N)
if n == N:
    print(n)
else:
    print(n+1)
