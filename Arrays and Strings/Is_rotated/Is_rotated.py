#function to check whether the given string s2 is a rotated version of the
#string s1 eg erbottlewat is a rotated version of waterbottle
def is_rotate(s1,s2):
#the string s1 and its rotated version should have the same length if not it is
#s2 is certainly not a rotated version of s1
    if len(s1) != len(s2) :
        return False
#suppose we are given two strings s1 and another string s2
#s1 = waterbottle s2 = erbottlewat
#the string s1 is rotated about the 3rd character
#if we consider s2 + s2  erbottlewaterbottlewat we find the string s1
#(waterbottle) is a substring of s2 + s2 (erbottle\'waterbottle\'wat)
#therfore the condition to check whether a string s2 is a roted version of s1
#is equivalent to checking whether s1 is a substring of s2+s2
    return s1 in s2+s2
