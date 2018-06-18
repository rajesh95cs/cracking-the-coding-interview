#import every function and attributes from the file strpermutation
from strpermutation import *
#open the text file containing the test cases and read from it and store it
#object f
f = open('testcase.txt','r')
#use readlines() to read all the lines from the file and it is stored in
#as a list variable test_cases
test_cases = f.readlines()
#loop through the list (test_cases) which contain the test cases
for test_case in test_cases:
#split the string variable test_case using split() with space as the delimiter
#the output should contain a list of three strings , the first two elements of
#this list are the inputs to the test case and the last string element is the
#desired output for the test case , which is a boolean in string format
	in_out = test_case.split()
#creating a boolean variable out containing the output corresponding desired
#output of the test case (in_out[2] is the desire output of the test case )
	if in_out[2] == 'true':
#store the desired output in out which is a boolean variable as True  if the
#in_out[2] reads "true"
		out=True
	if in_out[2] == 'false':
#store the desired output in out which is a boolean variable as False  if the
#in_out[2] reads "false"
		out=False

	print("Test case ")
	print("First input: %s", in_out[0])
	print("Second input: %s", in_out[1])
#check whether return value of the function matches the desired output of the
#test case
	if str_permutation(in_out[0], in_out[1]) == out:
		print("test case passed")
	else:
		print("test case failed")
