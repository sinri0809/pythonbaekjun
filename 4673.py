# lst = list(range(1, 101))
#
#
# def dn(number):
#     noselfnumberlst = []
#     noselfnumber = 0
#     while noselfnumber < 100:
#         noselfnumber = number + (number % 10)
#         while number > 10:
#             number //= 10
#             noselfnumber += (number % 10)
#
#         noselfnumberlst.append(noselfnumber)
#         number = noselfnumber
#     print(noselfnumberlst)
#
#     return noselfnumberlst
#
#
# if __name__ == "__main__":
#
#     removlst = set([])
#     for i in range(1, 101):
#         removlst.update(dn(i))
#
#     print(removlst)
    
    # for i in removlst:
    #     if i in lst:
    #         lst.remove(i)
    #
    # print(lst)
    #

# 2번째 시간 초과과
numbers = list(range(1, 10001))


def dn(number):
    lst = []
    while True:
        no_selfnumber = number + (number % 10)
        while number >= 10:
            number //= 10
            no_selfnumber += number % 10
        if no_selfnumber > 10000:
            break
        else:
            lst.append(no_selfnumber)
            number = no_selfnumber
    
    return lst


if __name__ == "__main__":
    count = 0
    j = numbers[count]
    
    while True:
        print(j)
        for i in dn(j):
            if i in numbers:
                numbers.remove(i)
        count += 1
        j = numbers[count]
        if j > 10000:
            break
    
    print(numbers)
    # print(dn(5))
