def utopianTree(n):
    sum_height = 0
    for i in range(n+1):
        if i%2 == 0:
            sum_height += 1
        else:
            sum_height *= 2
    return sum_height

t = 5
for i in range(t):
    n = int(raw_input())
    print utopianTree(n)
