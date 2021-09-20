# numbers = list(range(1, 1001))
set_numbers = set(range(1, 10001))

def dn(number):
    lst = []
    str_number = str(number)
    while True:
        no_selfnumber = int(str_number)
        for s in str_number:
            no_selfnumber += int(s)
        if no_selfnumber > 10000:
            break
        else:
            lst.append((no_selfnumber))
            str_number = str(no_selfnumber)
        
    return lst
    

if __name__ == "__main__":

    checkset = set([])
    for i in range(1, 10000):
        if i not in checkset:
            set_numbers -= set(dn(i))
            checkset.update(dn(i))
            print(i)
            # print(dn(i))
            # print(checkset)
            # print()
        # print(sorted(lst_numbers))
    # print(dn(2))
    # # print(dn(3))
    # lst_numbers = list(set_numbers)
    # # lst_numbers.sort()
    # print(sorted(lst_numbers))
