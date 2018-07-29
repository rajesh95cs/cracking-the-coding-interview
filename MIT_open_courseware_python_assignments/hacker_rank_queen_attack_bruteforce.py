
def queenAttack(n,k,r_q,c_q,obstacles):
    count = 1
##right
    for i in range(c_q+1,n+1):
        if [i, r_q] in obstacles:

            break
        else:
            count += 1
    print "count 1 ", count

##left
    for i in range(c_q-1,0,-1):
        if [i,r_q] in obstacles:
            break
        else:
            count += 1
    print "count 2 ", count

##upward
    for i in range(r_q-1,0,-1):
        if [c_q,i] in obstacles:
            break
        else:
            count += 1
    print "count 3 ", count
##downward
    for i in range(r_q+1,n+1):
        if [c_q,i] in obstacles:
            break
        else:
            count += 1
    print "count 4 ", count
##upward right
    for i,j in zip(range(c_q+1,n+1),range(r_q+1,n+1)):
        if [i,j] in obstacles:
            break
        else:
            count += 1
    print "count 5 ", count
##upward left
    for i,j in zip(range(c_q+1,n+1),range(r_q-1,0,-1)):
        if [i,j] in obstacles:
            break
        else:
            count += 1
    print "count 6 ", count
##downward right
    for i,j in zip(range(c_q-1,0,-1),range(r_q+1,n+1)):
        if [i,j] in obstacles:
            break
        else:
            count += 1
    print "count 7 ", count
##downward right
    for i,j in zip(range(c_q-1,0,-1),range(r_q+1,0,-1)):
        if [i,j] in obstacles:
            break
        else:
            count += 1
    print "count 8 ", count
    print count

n = 5
k = 3
r_q = 3
c_q = 4
obstacles = [[5,5],[4,2],[2,3]]
queenAttack(n,k,r_q,c_q,obstacles)
