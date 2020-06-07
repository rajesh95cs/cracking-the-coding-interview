#Program to execute merge sort() by dividing the list and copying the halfs to two seperate lists
# and using those two seperate list as arguments to call the same fuction recursively


def merge(L,R):
    n = len(L)+len(R)
    new_arry = []
    i = 0
    j = 0
    for k in range(n):
        if i >= len(L) or j >= len(R):
            break
        if L[i] < R[j]:
            new_arry.append(L[i])
            i+=1
        else:
            new_arry.append(R[j])
            j+=1
    while i < len(L):
        new_arry.append(L[i])
        i+=1
    while j < len(R):
        new_arry.append(R[j])
        j+=1
    return new_arry

# this fuction does the merge sort
def mergesort(a):
    n = len(a)
    if(n==1):
        return a
    else:
        #two seperate lists are created from the existing list
        a1 = []
        for i in range(0,len(a)/2):
            a1.append(a[i])
        #print "a1:"+ str(a1)
        a2 = []
        for i in range(len(a)/2,len(a)):
            a2.append(a[i])
        #print "a2:"+ str(a2)
        a_1 = mergesort(a1)
        #print "a1:"+str(a1)
        a_2 = mergesort(a2)
        #print "a2:"+str(a2)
        return merge(a_1,a_2)

#a = [6,2,7,3,1,9,4,2]
#b = mergesort(a)
#print "sorted array" + str(b)
