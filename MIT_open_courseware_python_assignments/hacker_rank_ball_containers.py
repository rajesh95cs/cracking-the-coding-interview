def organizingContainers(container):
    l = len(container)
    m = len(container[0])
    row_sum = [0]*m
    col_sum = [0]*l
    for i in range(l):
        for j in range(m):
            row_sum[i] += container[i][j]
    for i in range(l):
        for j in range(m):
            col_sum[i] += container[j][i]

    if row_sum.sort() == col_sum.sort():
        print "possible"
    else:
        print "impossibe"





container = [[2,1],[0,0]]
organizingContainers(container)
