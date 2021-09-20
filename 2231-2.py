n = int(input())


def make_num_sum(number):
    str_num = str(number)
    result = number
    for i in str_num:
        result += int(i)
    return result


if __name__ == "__main__":
    for i in range(n-45, n+1):
        if make_num_sum(i) == n:
            print(i)
            break
        elif i == n:
            print(0)


#0.052
