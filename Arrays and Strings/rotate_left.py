def rotLeft(a, d):
    n = len(a)
    rot_array = []
    for i in range(n):
        rot_array.append(0)

    for i in range(n):
        j = (i+(n-d))%n
        rot_array[j] = a[i]
        #print rot_array[j]
    return rot_array

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
d = 100
print(rotLeft(a,d))
