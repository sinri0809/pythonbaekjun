t = int(input())
lstn = list(map(int, input().split()))

def simplejudge1(number):
    check = 0
    for i in range(1, number + 1):
        if number % i == 0:
            check += 1
    
    if check == 2:
        return True
    else:
        return False


def simplejudge2(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1
    


def judgeprime(number):
    
    lstprime_end = [1, 3, 7, 9]
    
    
    
    
if __name__ == "__main__":
    lstn.sort()
    if lstn[0] == 1:
        del lstn[0]
    
    count = 0
    lstprime = (2, 3, 5)
    lstprime_end = (1, 3, 7, 9)
    for num in lstn:
        if num in lstprime:
            count += 1
        elif num % 2 == 0:
            break
        elif num % 10 in lstprime_end:
            count += simplejudge2(num)
        
    
    print(count)
