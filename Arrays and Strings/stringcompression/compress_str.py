#function compress to compress a string
#for eg aaabbbbcccccc can be converted to a string a3b4c5
def compress(input_string):
# a list variable compress_str to store the output , the variable is
#initialised as an empty list,finally the list will be converted to
#a string
    compress_str = []
# a counter variable count is used to count number of occurance of character
#adjacent to it in the input string  str
    count = 1
#loop through each character of the string
    for i in range(len(input_string)-1):
#check whether the adjacent characters of the input string are same
        if input_string[i] == input_string[i+1]:
#if the conditon is satisfied increment the count
            count += 1
        else:
#else append the character at the ith position of input_string to the list compress_str
            compress_str.append(input_string[i])
#append the count of the character in the ith position to the list compress_str
#the count is appended to the list after converting it to a string
            compress_str.append(str(count))
#reset the count variable to 1 in order to count the next set of repeating
#characters
            count = 1
#append the last repeating and its count to compress_str list
    compress_str.append(input_string[i])
    compress_str.append(str(count))
#check whether if length of the compressed string is  greater than the input
#string
    if len(compress_str) > len(input_string):
#if the condition is true return the input string
        return input_string
    else :
        c_str = ''.join(compress_str)
#return compress_str list after converting it to a string
        return c_str
