import copy
def bigger_greater(w):
    w_list = list(w)
    n = len(w)
    justgreater = "z"*n
    original_string = copy.deepcopy(w)

    # print n
    for i in range(n-1,-1,-1):
        sorted_sublist = sorted(w[i:],reverse = True)
        temp = w[:i] + "".join(sorted_sublist)
        print "temp ",temp
        if temp > original_string:
            # print "temp", temp
            return temp

    return "no answers"


file = open('test.txt','r')
data_s = file.readlines()[0].rstrip("\n\r")
print data_s
result = bigger_greater(data_s)

print result
