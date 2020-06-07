import merge_sort_indexing; reload(merge_sort_indexing)
import mergesort; reload(mergesort)
from merge_sort_indexing import *
from mergesort import *
import collections
import time

def test_mergesort(input,output):
    for_system = []
    for i in input:
        for_system.append(i)
    start_time = time.time()
    for_system.sort()
    end_time = time.time()
    execution_time_1 = end_time - start_time
    print "the execution_time_sort() "+str(execution_time_1)
    if collections.Counter(for_system) == collections.Counter(output):
        print "Test Passed"
    else:
        print "Test Failed"

    start_time = time.time()
    expected = mergesort(input)
    end_time = time.time()
    execution_time_2 = end_time - start_time
    print "the execution_time_mergesort() "+str(execution_time_2)
    if collections.Counter(expected) == collections.Counter(output):
        print "Test Passed"
    else:
        print "Test Failed"
    start_time = time.time()
    mergesort_indexing(input,0,len(input))
    end_time = time.time()
    execution_time_3 = end_time - start_time
    print "the execution_time_mergesort_indexing() "+str(execution_time_3)
    if collections.Counter(input) == collections.Counter(output):
        print "Test Passed"
    else:
        print "Test Failed"
    time_difference_1 = execution_time_2 - execution_time_3
    print "the time difference between mergesort() and mergesort_indexing() is ",abs(time_difference_1)
    time_difference_2 = execution_time_1 - execution_time_2
    print "the time difference between sort() and mergesort() is ",abs(time_difference_2)
    time_difference_3 = execution_time_1 - execution_time_3
    print "the time difference between sort() and mergesort_indexing() is ",abs(time_difference_3)


fname = "Test_case.txt"
lis = []
with open(fname, 'r') as f:
    for line in f:
        lis.append(line.split())
        lis = [line for line in lis if line != []]
test=lis[0]
testcase_number = int(test[0])
lis.pop(0)
#print(lis)
for ele in lis:
    for i in range(len(ele)):
        ele[i] = int(ele[i])
for j in range(testcase_number):
    input = lis[0]
    output = lis[1]
    #print(input)
    #print(output)
    test_mergesort(input,output)
    lis.pop(0)
    lis.pop(0)
