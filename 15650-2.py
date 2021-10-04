n, m = map(int, input().split())
temp = []


def permu(i):
    temp.append(i)
    if len(temp) == m:
        print(' '.join(map(str, temp)))
    else:
        for j in range(i+1, n+1):
            permu(j)
    temp.pop()
    
    
if __name__ == "__main__":
    for i in range(1, n+1):
        permu(i)
        temp.clear()
