

def min_arry(arr,low,high):
    if len(arr) == 0
        return "no element"
    if low == high :
        min = arr[low]
    else:
        mid = (low+high)/2
        left_mid = min_arry(arr,low,mid)
        right_mid = min_arry(arr,mid+1,high)
        if left_mid < right_mid:
            min = left_mid
        else:
            min = right_mid
    return min

a = [6,2,7,3,1,9,4,2]
mini =  min_arry(a,0,len(a)-1)
print "mini ",mini
