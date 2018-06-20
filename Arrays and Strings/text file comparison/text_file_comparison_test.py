import re
#import every function and attributes from the file strpermutation
from text_file_comparison import *
#open the text file containing the test cases and read from it and store it
#object f
f = open('testcases.txt','r')
#use readlines() to read all the lines from the file and it is stored in
#as a list variable test_cases
test_cases = f.readlines()
for test_case in test_cases:
    test_case = test_case.split()
#the file name of the 1st input is assigned to variable input_file1
#the text contained in the file corresponding to the file name contained in the
#variable will be parsed as list input to the function file file_comparisons
#for testing
    input_file1 = test_case[0]
#the file name of the 2nd input is assigned to variable input_file2
#the text contained in the file corresponding to the file name contained in the
#variable will be parsed as list input to the function file file_comparisons
#for testing

    input_file2 = test_case[1]
#an input1 variable is assigned with words contained in the file with the file
#name stored in input_file1 variable the text from the file is split using the
#delimiters (fullstop,semi colon ,colon ,coma,space,and pipe) and stored as a
#list of strings
    input1 = re.split('; |, |\*|\n|\ ',open(input_file1,'r').read())
#an input2 variable is assigned with words contained in the file with the file
#name stored in input_file2 variable the text from the file is split using the
#delimiters (fullstop,semi colon ,colon ,coma,space,and pipe) and stored as a
#list of strings
    
    input2 = re.split('; |, |\*|\n|\ ',open(input_file2,'r').read())
#output variable is assigned with desired output of the inputs and it is
#converted from string to integer
    output = int(test_case[2])
    print("\nTest case ")
    print("First input file name: ", input_file1)
    print("Second input file name: ", input_file2)

    if  file_comparisons(input1,input2) == output:
       print "test passed"
    else :
       print "test failed"
