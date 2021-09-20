t = int(input())
lstn = list(map(int, input().split()))

def judgeprime(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1


if __name__ == "__main__":
    lstn.sort()
    if lstn[0] == 1:
        del lstn[0]

    count = 0
    tplprime = (2, 3, 5)
    tplprime_end = (1, 3, 7, 9)
    for num in lstn:
        if num in tplprime:
            count += 1
            print("tplprime")
            
        elif num % 2 == 0:
            print("even number")
            pass
        
        elif num % 10 in tplprime_end:
            print("judge")
            count += judgeprime(num)

    print(count)
