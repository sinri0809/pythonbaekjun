import  sys

numb = int(input())
str = input()
sum = 0
for i in range(numb):
    sum += int(str[i])
print(sum)

# 짧은 코딩
n = int(input())
lst = map(int, input())
print(sum(lst))
