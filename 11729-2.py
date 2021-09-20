N = int(input())
global count
global memo

# 1 = 212
# 0 = 2
def hanoi_track(n, m, l, N):
    memo = [(n, m), ]
    
    if N >= 3:
        memo.append(hanoi_track(n, l, m, N-1))
    return memo



def hanoi_count(N):
    count = 1
    for i in range(N):
        count += count*2 + 1
    return count


if __name__ == "__main__":
    print(hanoi_count(N))
