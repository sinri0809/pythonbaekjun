import sys


n = int(input())
number_lst = [int(sys.stdin.readline()) for _ in range(n)]
# print(p_number_lst)
# 삽입 정렬 사용
sort_lst = [number_lst[0], ]
un_sort_lst = number_lst[1:]

for val in un_sort_lst:
    if val < sort_lst[0]: # 최하 값
        sort_lst.insert(0, val)
    elif sort_lst[len(sort_lst)-1] < val:
        sort_lst.append(val) # 최상 값
    else:
        for i in range(1, len(sort_lst)-1):
            if sort_lst[i-1] < val < sort_lst[i]:
                sort_lst.insert(i, val)
             
                
for temp in sort_lst:
    print(temp)
