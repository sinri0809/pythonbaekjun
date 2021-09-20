year = int(input())

a = [4, 100, 400]
s = []
for val in a:
    s.append(year % val)

# if s[0] == 0 and s[1] != 0:
#     print(1)
# elif s[0] == 0 and s[2] == 0:
#     print(1)
if s[0] == 0:
    if s[1] != 0 or s[2] == 0:
        print(1)
    else:
        print(0)
else:
    print(0)

# print(s)
