def Search(scores,element):
    first = 0
    last = len(scores)-1
    while first < last:
        mid = (first + last)/2
        if scores[mid] == element:
            return (mid,True)
        else:
            if element > scores[mid]:
                last = mid - 1
            else:
                first  = mid + 1
    if scores[first] == element:
        return (first,True)
    else:
        return (first,False)


def climbingLeaderboard(scores,alice):
    ranklist = []
    rank = 1
    n = len(scores)
    for i in range(n-1):
        ranklist.append(rank)
        if scores[i] > scores[i+1]:
            rank += 1

    ranklist.append(rank)

    rank = []
    m = len(alice)
    for element in alice:
        ranktrack = Search(scores,element)
        if ranktrack[1] is True:
            rank.append(ranklist[ranktrack[0]])
        else:
            if element < scores[ranktrack[0]]:
                rank.append(ranklist[ranktrack[0]]+1)
            else:
                rank.append(ranklist[ranktrack[0]])

    print rank




if __name__ == '__main__':

    f = open('input.txt','r')
    score = f.readline()
    score = map(int, score.rstrip().split())
    alice = f.readline()
    alice = map(int,alice.rstrip().split())

    #print(score)
    #print(alice)
    f.close()
    climbingLeaderboard(score,alice)
