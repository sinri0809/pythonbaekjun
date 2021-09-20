# ~2439
number = int(input())

for val in range(1, number+1):
    print(" " * (number-val), end="")
    print("*" * val)


