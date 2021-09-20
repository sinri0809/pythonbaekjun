# 경우의 수가 두 개 있을 수도 있음..
# 모두 체크하는데,,, 조합 문제임. 부분집합 구하기...
import itertools


n, m = map(int, input().split())
card_lst = list(map(int, input().split()))

comb_lst = list(itertools.combinations((card_lst), 3))
sum_set = set()


for i in comb_lst:
    if sum(i) <= m:
        sum_set.add(sum(i))

print(max(sum_set))
