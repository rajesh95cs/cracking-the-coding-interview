def kangaroos(x1,v1,x2,v2):
    flag = 0
    while x1 != x2 :
        x1 = x1 + v1
        x2 = x2 + v2
        flag = 1
        if x1 > 1000 and x2 > 1000:
            flag = 0
            break
    if flag == 1:
        print "YES"
    else:
        print "NO"

kangaroos(0,2,5,3)
