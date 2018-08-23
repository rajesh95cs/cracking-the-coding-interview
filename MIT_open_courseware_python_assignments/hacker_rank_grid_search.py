def gridSearch(g,p):

    str_p = ""
    for innerlist in p:
        for item in innerlist:
             str_p = str(str_p) + str(item)
        str_p += ' '
    c = str_p.split()
    print "c ",c
    str_g =""
    for innerlist in g:
        for item in innerlist:
             str_g = str(str_g) + str(item)
        str_g += ' '
    d = str_g.split()
    print "d ",d
    if len(c) > len(d) or len(c[0]) > len(d[0]):
        return "NO"
    ver_index = 0
    for item1 in d:

        if c[0] in item1:
            hor_index = item1.find(c[0])
            break
        ver_index += 1
    i = 0
    flag = 0
    for item2 in c:

        if item2 == d[ver_index+i][hor_index:len(item2)+hor_index]:
            print "item 2 ",item2
            print "d[ver_index+i][hor_index:hor_index+len(item2)] ",d[ver_index+i][hor_index:hor_index+len(item2)]
            flag = 1
        else:
            flag = 0
            print "No"

        i += 1


    if flag == 1:
        print "yes"
    else:
        print "no"

file = open('test.txt','r')
data_s = file.readlines()
G = []
del data_s[0]
data = data_s[0].split()
del data_s[0]
for i in range(int(data[0])):
    for j in range(int(data[1])):
        data_g = data_s[0].split()
        G.append(data_g)
        del data_s[0]
P = []
data = data_s[0].split()
del data_s[0]
for i in range(int(data[0])):
    for j in range(int(data[1])):
        data_p = data_s[0].split()
        P.append(data_p)
        del data_s[0]

print G
print P




#G = [[1,2,3,4,5,6,7,8,9,0],[0,9,8,7,6,5,4,3,2,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],
#[2,2,2,2,2,2,2,2,2,2]]
#P = [[8,7,6,5,4,3],[1,1,1,0,1,1],[1,1,1,1,1,1]]
gridSearch(G,P)
