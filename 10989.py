import sys


n = int(input())
number_arr = [int(sys.stdin.readline()) for _ in range(n)]
cnt_arr = [0 for _ in range(10001)]
output_arr = [0 for _ in range(n+1)]

for i in number_arr:
    cnt_arr[i] += 1
# print(cnt_arr)
for i in range(10000):
    cnt_arr[i+1] += cnt_arr[i]

# print(cnt_arr)
# print(number_arr)
# print(result_arr)

for i in number_arr:
    if cnt_arr[i] != 0:
        output_arr[cnt_arr[i]] = i
        cnt_arr[i] -= 1

for val in output_arr:
    if val != 0: # 자연수만 있기 때문에..
        print(val)
# print(result_arr)
