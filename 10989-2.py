import sys


n = int(input())
# input_arr = [int(sys.stdin.readline()) for _ in range(n)]
count_arr = [0 for _ in range(10001)] # 일단 0-100

for i in range(n):
    num = int(sys.stdin.readline())
    count_arr[num] += 1

for i in range(10001):
    if count_arr[i] != 0:
        for j in range(count_arr[i]):
            print(i)




#
# for idex in range(10000):
#     count_arr[idex+1] += count_arr[idex]
#
# output_arr = [0] * (n+1)
#
# # for val in input_arr:
# #     output_arr[count_arr[val]] = val
# #     count_arr[val] -= 1
# for val in count_arr:
#     if val != 0:
#         print()
#
