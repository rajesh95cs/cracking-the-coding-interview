
def partition(arry,low,high):
    i = low-1
    pivot = arry[high]
    for j in range(low,high):
        if arry[j] <= pivot:
            i += 1
            arry[i],arry[j] = arry[j],arry[i]

    arry[i+1],arry[high] = arry[high],arry[i+1]
    return ( i+1 )



def quicksort(arry,low,high):
    if low < high:
        p_index = partition(arry,low,high)
        quicksort(arry,low,p_index-1)
        quicksort(arry,p_index+1,high)

#a = [6,2,7,3,1,9,4,2]
#quicksort(a,0,len(a)-1)
#print "sorted array ",a
