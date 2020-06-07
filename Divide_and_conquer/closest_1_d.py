
def closest(arr,low,high):
    if high - low == 1:
        return abs(arr[high]-arr[low])

    if low < high:
        mid = (low + high)/2
        dl = closest(arr,low,mid)
        dr = closest(arr,mid+1,high)

        d = min(dl,dr)
        b = min(abs(arr[mid]-arr[mid+1]),d)
        return b

a = [4,2,7,1]
a.sort()
answer = closest(a,0,len(a)-1)
print "answer = ",answer
