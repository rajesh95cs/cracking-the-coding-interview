


def arrayManipulation(n, queries):
    list = [0]*(n+1)
    for query in queries:
        list[query[0]-1] += query[2]
        list[query[1]] -= query[2];
    max = x = 0
    for i in list:
        x=x+i;
        if(max<x): max=x;
return(max)
