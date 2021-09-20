n = int(input())

number_lst = []
for i in range(n):
    number_lst.append(input())
    

# number_lst = [int(input()) for _ in range(n)]

number_lst.sort()
print(number_lst)
for i in number_lst:
    print(i)
