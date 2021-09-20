N = int(input())
n = N
count = 0

while True:
    n1 = n // 10
    n2 = n % 10
    n3 = (n1 + n2) % 10
    n = n2 * 10 + n3
    
    count += 1
    # print(n)
    if n == N:
        break
        
        
print(count)
