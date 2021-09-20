n = 9
s1 = '*'*3
s2 = '*'+' '+'*'
lst = [s1, s2, s1]

for i in lst:
    print(i)
#     ---
lst2 = []
for i in lst:
    lst2.append(i*3)
for i in lst:
    lst2.append(i+' '*3+i)
for i in lst:
    lst2.append(i*3)

for i in lst2:
    print(i)
#     ----
lst3 = []
for i in lst2:
    lst3.append(i*3)
for i in lst2:
    lst3.append(i+' '*9+i)
for i in lst2:
    lst3.append(i*3)

for i in lst3:
    print(i)
