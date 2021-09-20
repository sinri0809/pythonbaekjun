# N = int(input())
N = 10  # 홀수만 먼저 생각해보자. 3,5,7...
# lst_temp = []


def hanoi_track(n, m, l, N):
    if N == 1:
        print(n, m)
        return
    if N == 2:
        print(n, l)
        print(n, m)
        print(l, m)
        
        return
    else:
        hanoi_track(n, l, m, N-1)
        hanoi_track(n, m, l, N-2)
        hanoi_track(l, m, n, N-1)
        return
    
#
# def hanoi_count(N):
#     if N == 1:
#         return 1
#     else:
#         return hanoi_count(N-1)*2 + 1


if __name__ == "__main__":
    # print(hanoi_count(N))
    hanoi_track(1, 3, 2, N)
    # for i in lst_temp:
    #     print(' '.join(map(str, i)))

