n = int(input())


def star_p(n):
    lst_temp = []
    if n == 3:
        s1 = '*'*3
        s2 = '*'+' '+'*'
        lst = [s1, s2, s1]
        return lst
    for i in star_p(n//3):
        lst_temp.append(i*3)
    for i in star_p(n//3):
        lst_temp.append(i+' '*(n//3)+i)
    for i in star_p(n//3):
        lst_temp.append(i*3)
    return lst_temp


print('\n'.join(map(str, star_p(n))))
