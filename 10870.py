n = int(input())

f0 = 0
f1 = 1
f2 = f0 + f1
f3 = f2 + f1

def fibona(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibona(num - 2) + fibona(num - 1)


if __name__ == "__main__":
    print(fibona(n))
