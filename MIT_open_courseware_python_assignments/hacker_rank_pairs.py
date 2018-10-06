def pairs(k,arr):
    arr.sort()
    count = 0
    i = 0
    j = 1
    while j < n:
        diff = arr[j] - arr[i]
        if diff == k :
            count += 1
            j += 1
        elif diff > k :
            i += 1
        elif diff < k :
            j += 1
    return count        
k = 2
arr = [1,5,3,4,2]
pairs(k,arr)
