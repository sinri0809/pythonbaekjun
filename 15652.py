# n, m = map(int, input().split())
temp = list()
n = 4
m = 3


def func(next_num):
    temp_len = len(temp)
    if temp_len == m:
        print(' '.join(map(str, temp)))
    else:
        for i in range(next_num, n + 1):
            temp.append(i)
            func(i)
    temp.pop()


if __name__ == "__main__":
    for i in range(1, n+1):
        temp.append(i)
        func(i)
        temp.clear()
        


