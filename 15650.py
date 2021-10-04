# n까지 숫자 중에서 m개를 고른 수열
# 1<= m, n <=8
# n, m = map(int, input().split())
n = 5
m = 3
temp = []


def permu(i):
    temp.append(i)
    if len(temp) == m:
        # print('check')
        print(temp)
        # temp.pop()
    else:
        for j in range(i+1, n+1):
            # print(j)
            permu(j)
    temp.pop()


if __name__ == "__main__":
    for i in range(1, n+1):
        # print(i)
        permu(i)
        temp.clear()

# for i in range(1, m+1):
#     for j in range(i+1, n+1):
#         for k in range(j+1, n+1):
#             print(i, j, k)
