n = int(input())
# 한수 인지 알아내야함.
count = 0
if n < 100:
    count = n
    # 100 미만은 모두 한수다.
else:
    count += 99
    for temp in range(100, n+1):
        s = set([])
        while temp >= 10:
            s1 = ((temp % 100) // 10) - (temp % 10)
            temp //= 10
            s.add(s1)
        if len(s) == 1:
            count += 1

print("{}".format(count))
