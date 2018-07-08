def packages():
    n = input("enter the min number of nuggets ")
    flag = 0
    for l in range(6):
        for i in range((n+l)/6):
            for j in range((n+l)/9):
                for k in range((n+l)/20):
                    if 6*i + 9*j +20*k == n+l:
                        flag = flag|2**l
    if flag == (2**6)-1:
        print "consecutive solutions exist for "+ str(n)
    else:
        print "no consecutive solution exist for "+str(n)


packages()
