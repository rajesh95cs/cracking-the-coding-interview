


def merge(arry,low,mid,high):
    temp = []
    i = low
    j = mid
    size = high - low
    for k in range(size):
        if i >= mid or j >= high:
            break
        if(arry[i] < arry[j]):
                temp.append(arry[i])
                i += 1
        else:
            temp.append(arry[j])
            j += 1
    while i < mid:
        temp.append(arry[i])
        i+=1
    while j < high:
        temp.append(arry[j])
        j+=1
    i = low
    for p in temp:
        arry[i] = p
        i += 1

    return arry



def mergesort_indexing(arry,low,high):
    if low < high-1:
        mid = (low + high)/2
        mergesort_indexing(arry,low,mid)
        mergesort_indexing(arry,mid,high)



        merge(arry,low,mid,high)




a = [8,4,2,1]
mergesort_indexing(a,0,len(a))
print "sorted array ",a
