n = int(input())

dct = dict()
for _ in range(n):
    x, y = map(int, input().split())
    if x in dct:
        dct[x].add(y)
    else:
        dct[x] = {y, }
        

if __name__ == "__main__":
    set_keys = sorted(dct.keys())
    for i in set_keys:
        for j in sorted(dct[i]):
            print(i, j)
