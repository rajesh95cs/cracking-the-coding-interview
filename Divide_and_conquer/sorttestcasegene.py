import random


def sort_test_case(length):


    f = open("Test_case.txt","w")
    f.write(str(length)+"\n\n")
    for j in range(length):
        n = random.randint(1,1000000)
        sorted_array = []
        f = open("Test_case.txt","a")
        for i in range(n):
            sorted_array.append(random.randint(1,1000))
            #print "each element"+ str(random_array)
        for j in sorted_array:
            f.write(str(j)+" ")
        sorted_array.sort()
        f.write("\n")
        for k in sorted_array:
            f.write(str(k)+" ")
        f.write("\n\n")
        #print "random array" +str(random_array)
        #print "sorted_array" + str(sorted)
        #sorted_array.append(sorted)

    f.close()

sort_test_case(1)
