a, b = map(int, input().split())


if __name__ == "__main__":
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')
