# n, m = map(int, input().split())
n = 4
m = 4
lst = [i for i in range(1, n+1)]
# print(lst) [1, 2, 3, 4]
issued = [False for _ in range(n)]
k = 0
arr = [0 for _ in range(m)]


def plus(i):
    issued[i-1] = True


def sub(i):
    issued[i-1] = False
    
    
def make_arr(k):
    temp = 0

    for i in lst:
        if not issued[i-1] and k < 4:
            plus(i)
            arr[k] = i
            k += 1
            temp = i
            print(issued)
            print(arr)
    if k == 4:
        k -= 2
        sub(temp)
        print(issued)
        make_arr(k)
        
        
make_arr(k)
# if __name__ == "__main__":
#     k = 0
#     make_arr(k)
    
