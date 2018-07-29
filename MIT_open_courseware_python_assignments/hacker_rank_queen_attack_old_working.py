def queenAttack(k,n,rq,cq,obstacles):
    queen_movement_dict = {}
    queen_boundaries_dict = {}
    directions = ["top","down","left","right","topright","topleft","downright","downleft"]
    for direction in directions:
        queen_movement_dict[direction] = 10*n


    for [j,i] in obstacles:
        #top
        if i == cq and j > rq:
            distance = abs(j - rq)-1
            queen_movement_dict["top"] = min(distance,queen_movement_dict["top"])
            continue
        #print queen_movement_dict["top"]
        #down
        if i == cq and j < rq:
            distance = rq-j-1
            print "j = ",j
            queen_movement_dict["down"] = min(distance,queen_movement_dict["down"])
            continue
        #print queen_movement_dict["down"]

        #left
        if i < cq and j == rq:
            distance = cq -i -1
            print"left distance ",distance
            queen_movement_dict["left"] = min(distance,queen_movement_dict["left"])
            continue
        #print queen_movement_dict["left"]

        #right
        if i > cq and j == rq:
            distance = abs(i - cq)-1
            queen_movement_dict["right"] = min(distance,queen_movement_dict["right"])
            continue
        #print queen_movement_dict["right"]
        #topright
        if i > cq and j > rq and (int((j-rq)/(i-cq))==1):
            distance = i - cq-1
            queen_movement_dict["topright"] = min(distance,queen_movement_dict["topright"])
            continue
        #print queen_movement_dict["topright"]
        #topleft
        if i < cq and j > rq and (int((j-rq)/(i-cq))==-1):
            distance = cq - i-1
            queen_movement_dict["topleft"] = min(distance,queen_movement_dict["topleft"])
            continue
        #print queen_movement_dict["topleft"]
        #downright
        if i > cq and j < rq and (int((j-rq)/(i-cq))==-1):
            distance = rq-j-1
            queen_movement_dict["downright"] = min(distance,queen_movement_dict["downright"])
            continue
        #print queen_movement_dict["downright"]
        #downleft
        if i < cq and j < rq and (int((j-rq)/(i-cq))==1):
            distance = rq - j-1
            queen_movement_dict["downleft"] = min(distance,queen_movement_dict["downleft"])
            continue
        #print queen_movement_dict["downleft"]
    queen_boundaries_dict["top"] = abs(rq - n)
    queen_boundaries_dict["down"] = abs(rq)-1
    queen_boundaries_dict["left"] = abs(cq)-1
    queen_boundaries_dict["right"] = abs(cq - n)
    queen_boundaries_dict["topleft"] = min(abs(cq-1),abs(rq-n))
    queen_boundaries_dict["topright"] = min(abs(cq - n),abs(rq-n))
    queen_boundaries_dict["downleft"] = min(abs(rq-1),abs(cq-1))
    queen_boundaries_dict["downright"] = min(abs(rq-1),abs(cq-n))

    for direction in directions:
        queen_movement_dict[direction] = min([queen_movement_dict[direction],queen_boundaries_dict[direction]])
    ways = sum(queen_movement_dict.values())

    print "queen_boundaries_dict ",queen_boundaries_dict

    print ways

file = open('test.txt','r')
data_s = file.readlines()
data = data_s[0].split()
n = int(data[0])
k = int(data[1])
data = data_s[1].split()
r_q = int(data[0])
c_q = int(data[1])
#print n,k,r_q,c_q
del data_s[0]
del data_s[0]
obstacles =[]
for data in data_s:
    data = data.split()
    obstacles.append([int(data[0]), int(data[1])])
#print len(obstacles)
queenAttack(k,n,r_q,c_q,obstacles)
