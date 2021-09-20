n = int(input())
# 1 ~ 1,000,000


def makenumsum(number):
    numstr = str(number)
    result = number
    for i in numstr:
        result += int(i)
    
    return result


#     brute force algorithms
if __name__ == "__main__":
    for i in range(1, n+1):
        if makenumsum(i) == n:
            print(i)
            break
        elif i == n:
            print(0)

        
