


def polyMult(p,q,n):
    if (n == 1):
        temp = p[0] * q[0]
        return temp


    d = n/2;
    pHigh = [0]*d
    qHigh = [0]*d
    pLow  = [0]*(d-(n%2))
    qLow  = [0]*(d-(n%2))

    for i in range(d):
        pHigh[i] = p[i+d]
        qHigh[i] = q[i+d]
        pLow[i] = p[i]
        qLow[i] = q[i]


    lowPQ = polyMult(pLow,qLow,d)

    lowPHighQ = polyMult(pLow,qHigh,d)

    lowQHighP = polyMult(pHigh,qLow,d)

    highPQ = polyMult(pHigh,qHigh,d)

    pq = [0]*((2*n)-1)

    print "lowpq ",lowPQ
    for i in range(n-1):
        pq[i] += lowPQ
        pq[i+d] += lowPHighQ + lowQHighP
        pq[i+(2*d)] += highPQ
    print "pq ",pq
    return pq

A = [4,1,2,7]
B = [2,1,8,3]
no_of_coeff = 4
print(polyMult(A,B,no_of_coeff))
