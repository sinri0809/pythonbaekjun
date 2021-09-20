import math as mt

lst_ABV = list(map(int, input().split()))
A = lst_ABV[0]
B = lst_ABV[1]
V = lst_ABV[2]

# 초기 조건 A-B>0
# x1 = (V-A) / (A-B) - 1
# x2 = V / (A-B)
#
# (A - B)
#
# print(x1)
# print(x2)
#
# print(int(min(x1, x2)))
n = mt.ceil(((V-A)/(A-B)) + 1)

print(n)
