# M과 N이 같을 때를 유의해야한다.
t_lst = list(map(int, input().split()))
n1 = int(t_lst[0])
n2 = int(t_lst[1])


def prime_list(number):
    sieve = [True] * (number +1)
    sieve[1] = False
    if number > 99:
        m = int(number ** 0.5) + 1
    else:
        m = number
    
    for i in range(2, m + 1):
        if sieve[i]:
            # print(i)
            for j in range(i+i, number + 1, i):
                sieve[j] = False
    
    return sieve
    
    
     
if __name__ == "__main__":

    lst = prime_list(n2)
    for i in range(n1, n2 + 1):
        if lst[i]:
            print(i)
