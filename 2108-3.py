count_arr = [0 for _ in range(8001)]
sort_arr = []


if __name__ == "__main__":
    n = int(input())
    sum = 0
    min_input = 4000
    max_input = -4000
    
    for val in range(n):
        temp = int(input())
        if temp < min_input:
            min_input = temp
        if temp > max_input:
            max_input = temp
        sum += temp
        count_arr[temp+4000] += 1

    mode = max(count_arr)
    mode_index = count_arr.index(mode)
    
    for i in range(min_input, max_input+1):
        if count_arr[i+4000] != 0:
            for j in range(count_arr[i+4000]):
                sort_arr.append(i)
    
    for i in range(mode_index+1, max_input+4001):
        if count_arr[i] == mode:
            mode_index = i
            break
    
    # print(sort_arr)
    
    
    print(sum//n)
    print(sort_arr[(n-1)//2])
    print(mode_index-4000)
    print(sort_arr[n-1] - sort_arr[0])
