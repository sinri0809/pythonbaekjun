# 최대 100,000개 좌표
n = int(input())
# {x:{y1,y2...}, x2:{y1,y2...}}
dct = dict()
# input
for _ in range(n):
    x, y = map(int, input().split())
    if x in dct:
        dct[x].add(y)
    else:
        dct[x] = {y, }


if __name__ == "__main__":
    print(dct)
    temp_x = int()
    
    set_keys = sorted(set(dct.keys()))
    # set_keys = list(set(dct.keys()))
    # for _ in range(len(set_keys)):
    #     temp_x = set_keys.pop()
    #     if temp_x >= 0:
    #         break
    
    for i in set_keys:
        # print(i)
        # sorted(dct[i])
        # print(sorted(dct[i]))
        for j in sorted(dct[i]):
            print(i, j)

