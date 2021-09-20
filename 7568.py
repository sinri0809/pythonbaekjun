# -*- coding: utf-8 -*-
# N 2~50
# x,y 10~200

N = int(input())
lst = []
lst_count = [1 for _ in range(N)]

for i in range(N):
    lst.append(tuple(map(int, input().split())))


for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if((lst[i][0] < lst[j][0]) and (lst[i][1]<lst[j][1])):
            lst_count[i] += 1
        elif((lst[i][0] > lst[j][0]) and (lst[i][1]>lst[j][1])):
            lst_count[j] += 1


print(' '.join(str(i) for i in lst_count))
