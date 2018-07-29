def acm_icpc(topic):
    known = 0
    max_known = 0
    know_all = 0
    n = len(topic)
    m = len(topic[0])
    for i in range(n-1):
        for j in range(i+1,n):
            known = 0
            for k in range(m):
                if topic[i][k] == 1 or topic[j][k] == 1:
                    known += 1
                if max_known < known:
                    max_known = known
                    know_all = 0
                if max_known == known:
                    know_all += 1

    print "max_known ",max_known,"known all ",know_all

topic = [[1,0,1,0,1],[1,1,1,0,0],[1,1,0,1,0],[0,0,1,0,1]]

acm_icpc(topic)
