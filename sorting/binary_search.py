def binary_search(arr,low,high,ele):
    if(len(arr) == 0):
        return "array is empty"
    elif(len(arr) == 1):
        if(ele == arr[0]):
            return "element found at 0"
        else:
            return "element not found"
    elif(len(arr) == 2):
        if (ele == arr[0]):
            return "element found at 0"
        elif(ele == arr[1]):
            return "element found at 1"
        else:
            return "element not found"
    else:
        if low < high :
            mid = (low+high)/2
            if(arr[mid] == ele):
                return "element found at",mid
            binary_search(arr,low,mid-1,ele)
            binary_search(arr,mid+1,high,ele)

a = [6,2,7,3,1,9,4,2]
a_dict = {}
for i in range(len(a)):
    a_dict[i] = a[i]
print a_dict

a.sort()
b = binary_search(a,0,len(a)-1,3)
print b
