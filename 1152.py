str1 = str(input().strip())
# print(str1)
str2 = str1.split(' ')
if '' in str2:
    str2.remove('')

print(len(str2))
# 공백을 새는 경우도 있다.
