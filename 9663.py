from pprint import pprint
# n = int(input())
# example
n = 5
row = col = n
arr = [[0 for col_i in range(col)] for row_i in range(row)]
count = 0

temp_lst = list()
for row in arr:
    i = arr.index(row)
    for j in range(n):
        if row[j] == 0:
            row[j] = -1
            for temp_j in range(j+1, n):
                arr[i][temp_j] = 1
                for temp_i in range(i+1, n):
                    arr[temp_i][j] = 1
            pprint(arr, indent=2, width=20)


# 한번 돌기
# for row in arr:
#     row_index = arr.index(row)
#     for i in range(n):
#
#         # flag가 안띄어졌을 때,
#         if row[i] == 0:
#             row[i] = -1
#             print("row=", row_index, "i=",i,)
#             temp = row_index
#             for j in range(i+1, n-1):
#                 arr[row_index][j] = 1
#                 arr[j][i] = 1
#
#                 temp += 1
#                 print(temp)
#                 arr[temp][j] = 2
#                 # arr[temp][j] = 2
#                 # arr[j][j] = 1
#             pprint(arr, indent=2, width=20)





