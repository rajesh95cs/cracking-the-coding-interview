



def max_arry(arr,low,high):
    if len(arr) == 0:
        return "no element"
    if low == high :
        max = arr[low]
    else:
        mid = (low+high)/2
        left_mid = max_arry(arr,low,mid)
        right_mid = max_arry(arr,mid+1,high)
        if left_mid > right_mid:
            max = left_mid
        else:
            max = right_mid
    return max

a = [6,2,7,3,1,9,4,2]
maxi =  max_arry(a,0,len(a)-1)
print "maxi ",maxi
