from itertools import permutations


n, m = map(int, input().split())

# 순열 이용한 코드
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(' '.join(map(str, i)))

visited = [False for _ in range(n)]
arr = []


def make_arr(k, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            make_arr(k+1, n, m)
            visited[i] = False
            arr.pop()
            

make_arr(0, n, m)
