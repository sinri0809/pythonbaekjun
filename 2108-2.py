p_count_arr = [0 for _ in range(4001)]
n_count_arr = [0 for _ in range(4000)]
sort_arr = []


def put_count(num):
    if num >= 0:
        p_count_arr[num] += 1
    else:
        n_count_arr[num+4000] += 1


if __name__ == "__main__":
    n = int(input())
    sum = 0
    
    for val in range(n):
        temp = int(input())
        sum += temp
        put_count(temp)
    
    
    
    
    if len(n_count_arr) != 0:
        for i in range(-4000, 0):
            if n_count_arr[i+4000] != 0:
                for _ in range(n_count_arr[i+4000]):
                    sort_arr.append(i)

    for i in range(4001):
        if p_count_arr[i] != 0:
            for _ in range(p_count_arr[i]):
                sort_arr.append(i)

        
    
    
    # print(sort_arr)
    
    print(sum//n)
    print(sort_arr[(n-1)//2])
    
    print(sort_arr[n-1] - sort_arr[0])
