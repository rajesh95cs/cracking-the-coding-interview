
# import all the functions and attributes from the file compress_str
from compress_str import *
#open the file test case
f = open("testcase.txt","r")
#use readlines() to read all the lines from the text file and store it in
#a list variable test_cases
test_cases = f.readlines()
#loop through the list (test_cases) which contains the testcases
for test_case in test_cases:
#split the string variable test_case using split() with space as the delimiter
#the output should contain a list of two strings , the first element of
#this list is the input to the test case and the last string element is the
#desired output for the test case , which is a string in the compressed format
    in_out = test_case.split()
#displaying the test cases in a desired format
    print("\ntest case")
    print("input : ",in_out[0])
    print("desired output : ",in_out[1])
#check whether the returned string value of the function matches with the
#desired output of the test case
    if compress(in_out[0]) == in_out[1]:
        print("test passed")
    else:
        print("test failed")
