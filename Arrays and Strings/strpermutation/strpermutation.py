#def str_permutation(str1,str2):
#    b = sorted(str1)
#    c = sorted(str2)
#    for i in range(len(b)):
#        flag = 0
#        if b[i] == c[i]:
#            flag = 1
#        else :
#            print("not a permutation")
#            break
#    if flag == 1:
#        print("str1 is a permutation of the other")
#
#
#str1 = 'agg'
#str2 = 'gaa'
#str_permutation(str1,str2)


#approach 2
def str_permutation(str1,str2):
    arr1 = []
    arr2 = []
    flag = 0
    if(len(str1) != len(str2)):
	return False
    for i in range(256):
        arr1.append(0)
        arr2.append(0)
    for j in range(0,len(str1)):
        arr1[ord(str1[j])] += 1
        arr2[ord(str2[j])] += 1
    for i in range(256):
        if arr1[i] == arr2[i]:
            flag = 1
        else:
            return False
            flag = 0
            break
    if flag == 1 :
        return True

str1 = 'adder'
str2 = 'ddare'
str_permutation(str1,str2)
