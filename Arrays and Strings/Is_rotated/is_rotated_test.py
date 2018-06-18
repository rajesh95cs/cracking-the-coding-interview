
# import all the functions and attributes from the file is_rotated.py to test
#the function is_rotate. The function accepts two inputs as string and returns
# a boolean value
from Is_rotated import *
#open the file testcases.txt to read the various test cases
f = open("testcases.txt","r")
#use readlines() to read all the lines from the text file and store it in
#a list variable test_cases
test_cases = f.readlines()
#loop through the list (test_cases) which contains the test cases
for test_case in test_cases:
#split the string variable test_case using split() with space as the delimiter
#the output should contain a list of three strings , the first and second
#element of this list is the input to the test case and the last string element is the
#desired output for the test case , which is a boolean in string format
    in_out = test_case.split()
#creating a boolean variable out containing the output corresponding desired
#output of the test case (in_out[2] is the desire output of the test case )
    if in_out[2] == 'True':
#store the desired output in out which is a boolean variable as True  if the
#in_out[2] reads "true"
		out=True
    if in_out[2] == 'False':
#store the desired output in out which is a boolean variable as False  if the
#in_out[2] reads "false"
		out=False
    print("\nTest case ")
    print("First input: %s", in_out[0])
    print("Second input: %s", in_out[1])
#check whether return value of the function matches the desired output of the
#test case
    if is_rotate(in_out[0], in_out[1]) == out:
        print("test case passed")
    else:
        print("test case failed")
