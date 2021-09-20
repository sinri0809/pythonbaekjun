# Break-even point
# A,B   C

costs = list(map(int, input().split()))
if (costs[2] - costs[1]) <= 0:
    print(-1)

else:
    i_point = round((costs[0] / (costs[2] - costs[1])), 3)
    i_point_int = (i_point // 1)
    
    # if i_point == i_point_int:
    print("{}".format(int(i_point_int+1)))
    # elif
    #

