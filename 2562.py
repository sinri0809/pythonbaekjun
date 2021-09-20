# 100보다 작은 자연수

arr = []
for _ in range(9):
    arr.append(int(input()))
    
# list 연산 사용시
n_max = max(arr)
n_max_idx = arr.index(n_max)
print(n_max)
print(n_max_idx+1)

# list 연산 사용 안할 시
