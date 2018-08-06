import math

def encryption(s):
    s_without_space = "".join(s.split())
    #print "s_without_space ",s_without_space
    l = len(s_without_space)

    min_area = math.ceil(math.sqrt(l))*math.ceil(math.sqrt(l))
    mindimensions = (int(math.ceil(math.sqrt(l))),int(math.ceil(math.sqrt(l))))
    for col in range(int(math.floor(math.sqrt(l))),int(math.ceil(math.sqrt(l))+1)):
        for row in range(int(math.floor(math.sqrt(l))),col + 1):
            area = row * col
            if area >= l and area < min_area:
                min_area = area
                mindimensions = (row , col)
    encryption_matrix = []
    for i in range(mindimensions[0]):
        inside_encrypt = []
        for j in range(mindimensions[1]):
            inside_encrypt.append(" ")
        encryption_matrix.append(inside_encrypt)

    #print "encryption_matrix "
    count = 0
    flag = False
    for i in range(mindimensions[0]):
        for j in range(mindimensions[1]):
            encryption_matrix[i][j] = s_without_space[count]
            #print "encryption_matrix ",encryption_matrix
            #print "i ",i
            #print "j ",j
            #print "s_without_space[count] ",s_without_space[count]
            count += 1
            if count == len(s_without_space):
                flag = True
                break
        if flag is True:
            break
    #print "encryption_matrix ",encryption_matrix
    #print "mindimensions ",mindimensions
    encrypted_list = []
    for i in range(mindimensions[1]):
        for j in range(mindimensions[0]):
            if encryption_matrix[j][i] == " ":
                break
            encrypted_list.append(encryption_matrix[j][i])
        encrypted_list.append(" ")
    return "".join(encrypted_list)

file = open('test.txt','r')
data_s = file.read()
result = encryption(data_s)
print result
