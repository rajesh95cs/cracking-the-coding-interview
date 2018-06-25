def makeAnagram(a, b):
    list1 = [0]*256
    list2 = [0]*256
    remove_tracker = 0
    for i in range(len(a)):
        list1[ord(a[i])] += 1
    for i in range(len(b)):
        list2[ord(b[i])] += 1
    for i in range(256):
        if list1[i] != list2[i]:
            if list1[i] == 0 :
                remove_tracker += list2[i]

            elif list2[i] == 0:
                remove_tracker += list1[i]

            else:
                remove_tracker += abs(list1[i]-list2[i])

    print(remove_tracker)
#    return remove_tracker

a = "abc"
b = "cde"
makeAnagram(a,b)
