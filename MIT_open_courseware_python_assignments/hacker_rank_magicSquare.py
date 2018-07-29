import copy

def formingMagicSquare(s):
    temp = copy.deepcopy(s)
    char_count = []
    for i in range(10):
        char_count.append(0)
    for i in range(len(s)):
        for j in range(len(s[0])):
            char_count[s[i][j]] += 1
    print "before manipulation",char_count
    differ_list = 2*[50]

    cost_list = []
    for i in range(1,10):
        if char_count[i] == 0:
            differ_list = 2*[50]
            for j in range(i-1,0,-1):
                if char_count[j] > 1:
                    differ_list[0] = abs(j-i)
                    break
            for k in range(i+1,10):
                if char_count[k] > 1:
                    differ_list[1] = abs(k-i)
                    break
            print "differ_list ",differ_list
            min_ele = min(differ_list)
            if min_ele == differ_list[0]:
                char_count[i] += 1
                char_count[j] -= 1
                for a in range(len(temp)):
                    for b in range(len(temp[0])):
                        if temp[a][b] == j:
                            temp[a][b] = i
            if min_ele == differ_list[1]:
                char_count[i] += 1
                char_count[k] -= 1
                for a in range(len(temp)):
                    for b in range(len(temp[0])):
                        if temp[a][b] == k:
                            temp[a][b] = i
            cost_list.append(min_ele)
    print "original" , s
    print "magic square" ,temp
    print "cost_list", cost_list
    print "after manipulation", char_count

    print sum(cost_list)

s = [[4,5,8],[2,4,1],[1,9,7]]

#for _ in xrange(3):
#    s.append(map(int, raw_input().rstrip().split()))

formingMagicSquare(s)
