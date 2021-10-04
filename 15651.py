# n, m = map(int, input().split())
n = 3
m = 3
temp = []


def loop(count):
    count += 1
    if count == m:
        print()
    else:
        for i in range(1, n+1):
            print(i, end=' ')
            loop(count)
    
    
if __name__ == "__main__":
    count = 0
    loop(0)
