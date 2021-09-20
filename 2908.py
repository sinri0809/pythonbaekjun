# 문자열을 뒤집어서 크기를 따지자.
strlst = input().split()
# print(lst)
lst1 = []
lst2 = []

for j in strlst[0]:
    lst1.append(j)
for j in strlst[1]:
    lst2.append(j)
    
lst1.reverse()
lst2.reverse()

# print(lst1)
for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
        continue
    elif lst1[i] > lst2[i]:
        print("{0}{1}{2}".format(lst1[0], lst1[1], lst1[2]))
        break
    elif lst1[i] < lst2[i]:
        print("{0}{1}{2}".format(lst2[0], lst2[1], lst2[2]))
        break
