def min_swaps(q):
    last_index = len(q)-1
    count = 0
    for i in range(0,last_index):
        for j in range(0,last_index-(i)):
            if q[j] > q[j+1]:
                temp  = q[i]
                q[i]  = q[i+1]
                q[i+1] = temp
                count += 1
    return count

q = [2,3,4,1,5]
print(min_swaps(q))
