def minimumbribes(q):
        noof_bribes = 0
        for i in range(len(q)-1,-1,-1):
            if (q[i] - (i+1)) > 2:
                return "Too chaotic"

            for j in range(max([0,q[i] - 2]),i):
                if q[j] > q[i] :
                    noof_bribes += 1

        return noof_bribes

q = [5,1,2,3,7,8,6,4]
print(minimumbribes(q))
