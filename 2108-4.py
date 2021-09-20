import sys


n = int(input())
count_arr = [0 for _ in range(8001)]    # -4000[0] ~ 0[4000] ~ 4000[8001]
sorted_arr = []

# input
for i in range(n):
    temp = int(sys.stdin.readline())
    count_arr[temp+4000] += 1

mod_number = 0
for val in range(8001):
    if count_arr[val] != 0:
        sorted_arr.append(val-4000)
    if count_arr[val] > mod_number:
        mod_number = max(count_arr[val], mod_number)
        mod_index = val

        
sum_number = 0
mid_number = 0
index_number = -1
mid_flag = 0
mod_flag = 0
for i in sorted_arr: # 최대 8001갠데...
    sum_number += i * count_arr[i+4000]
    index_number += count_arr[i+4000]
    if index_number >= (n-1)//2 and mid_flag == 0:
        mid_number = i
        mid_flag = 1
    if count_arr[i+4000] == mod_number:
        if mod_flag == 1:
            mod_index = i + 4000
            mod_flag = 10
        elif mod_flag == 0:
            mod_flag += 1
            
        
        
    
    



print(sum_number)
print(mid_number)
print(mod_index)
print(sorted_arr[len(sorted_arr)-1] - sorted_arr[0])
