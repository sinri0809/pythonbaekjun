def putcount(num):
    if temp >= 0:
        p_count_arr[num] += 1
    else:
        n_count_arr[abs(num)] += 1


def whichmaxandmin(num):
    if num > mx:
        max = num
    elif num < mn:
        min = num



if __name__ == "__main__":
    n = int(input())
    p_count_arr = [0 for _ in range(4001)]
    n_count_arr = [0 for _ in range(1, 4001)]
    
    temp = int(input())
    sum = temp
    mx = temp
    mn = temp
    
    for _ in range(n):
        temp = int(input())
        sum += temp
        putcount(temp)
        whichmaxandmin(temp)
        
        
    print(sum//n)
    
    print(mx-mn)


