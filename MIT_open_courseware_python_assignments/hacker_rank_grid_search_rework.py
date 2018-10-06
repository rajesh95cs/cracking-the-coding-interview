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
            i = 0
            flag = 0
            count = 0
            for item2 in c:

                if item2 == d[ver_index+i][hor_index:len(item2)+hor_index]:
                    print "item 2 ",item2
                    print "d[ver_index+i][hor_index:hor_index+len(item2)] ",d[ver_index+i][hor_index:hor_index+len(item2)]
                    count += 1

                else:
                    count = count
                    break
                print "count ",count
                i += 1
            if count == len(c):
                flag = 1
                return "yes"
            else :
                flag = 0
        ver_index += 1

    if flag == 0:
        return "no"






file = open('test.txt','r')
data_s = file.readlines()
data = data_s[0].split()
n = int(data[0])
print "n ",n

del data_s[0]
for i in range(n):
    G = []
    data = data_s[0].split()
    l = int(data[0])
    print "l ",l

    for i in range(l):
        del data_s[0]
        data_g = data_s[0].split()
        int_data_g = map(int,data_g[0])
        G.append(int_data_g)

        #print "data_s after del ",data_s
    P = []
    del data_s[0]
    data = data_s[0].split()

    m = int(data[0])
    print "m ",m
    for i in range(m):
        del data_s[0]
        data_p = data_s[0].split()
        int_data_p = map(int,data_p[0])
        P.append(int_data_p)
    del data_s[0]
    print(gridSearch(G,P))



#G = [[1,2,3,4,5,6,7,8,9,0],[0,9,8,7,6,5,4,3,2,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],
#[2,2,2,2,2,2,2,2,2,2]]
#P = [[8,7,6,5,4,3],[1,1,1,0,1,1],[1,1,1,1,1,1]]
