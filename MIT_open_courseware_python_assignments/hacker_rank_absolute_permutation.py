def absolute_permutation(n,k):
    if k == 0:
        return [i+1 for i in range(n)]
    elif n % (2*k) != 0 or 2*k > n:
        return [-1]
    return [(i+1)+(1 if (i//k)%2==0 else -1)*k for i in range(n)]
