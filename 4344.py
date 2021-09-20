import sys
c = int(input())
lst = []
for val in range(c):
    lst.append(list(map(int, sys.stdin.readline().split())))

for cls in lst:
    number = cls[0]
    total = 0
    for score in range(1, number+1):
        total += cls[score]
    mean = total / number
    upper_student = 0
    for score in range(1, number+1):
        if cls[score] > mean:
            upper_student += 1
    ratio_upper_student = round((upper_student/number) * 100, 3)
    
    print('{0:.3f}%'.format(ratio_upper_student))
