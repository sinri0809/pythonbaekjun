import sys


# 이거는 진짜 하고 난 뒤에 그냥 답 봐야겠다.
n = int(input())    # 최대 500,000
count_arr = [0 for _ in range(8001)]    # -4000[0] ~ 0[4000] ~ 4000[8001]
# input
for i in range(n):
    temp = int(sys.stdin.readline())
    count_arr[temp+4000] += 1
    
sum_num = 0
index_number = -1
mid = {'flag': 0, 'number': 0}
mod = {'flag': 0, 'number': 0}
nums = []   # [0]: min [1]: max
temp_count = 0
for val in range(8001):     # 최대 8002
    if count_arr[val]:
        sum_num += (val-4000) * count_arr[val]

        if index_number == -1:
            nums.append(val-4000)
        
        if count_arr[val] > temp_count:
            temp_count = count_arr[val]
            
        index_number += count_arr[val]

        if index_number >= (n-1)//2 and mid['flag'] == 0:
            mid['number'] = val - 4000
            mid['flag'] = 1

        if index_number == n-1:
            nums.append(val-4000)
  


temp_number = count_arr.index(temp_count)
for i in range(temp_number+1, nums[1]+4000+1):
    if count_arr[i] == temp_count:
        temp_number = i
        break




print(round(sum_num/n))
print(mid['number'])
print(temp_number-4000)
print(nums[1]-nums[0])
