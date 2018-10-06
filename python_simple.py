a = int(raw_input())
b = int(raw_input())
c = abs(a-b)
print "a = ", a
print "b = ", b 
if a > b :
    a = a - c
    b = b + c
elif a < b :
    a = a + c
    b = b - c
print "a = ", a
print "b = ", b
