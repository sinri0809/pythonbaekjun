t_lst = list(map(int, input().split()))
n1 = t_lst[0]
n2 = t_lst[1]

if n2 > 99:
    m = int(n2 ** 0.5)
else:
    m = n2 + 1

n_lst = [True] * (n2 + 1)
n_lst[1] = False

for i in range(2, m):
    if n_lst[i]:
        for j in range(i + i, n2 + 1, i):
            n_lst[j] = False

for i in range(n1, n2 + 1):
    if n_lst[i]:
        print(i)
