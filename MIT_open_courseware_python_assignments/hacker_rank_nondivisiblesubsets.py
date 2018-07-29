import itertools

def nonDivisible_subsets(k,s):
    sets = set(s)
    print sets
    sum = 0
    total_divisible_subset = set([])
    nondivisible_subsets = set([])
    two_ele_subset_list = map(set,itertools.combinations(sets,2))

    for subset in two_ele_subset_list:
        #print "subset ",subset
        for d in subset:
            sum += d
        #    print"d "+str(d)
        #print "sum ",sum
        if sum % k == 0:
            print "sum ",sum
            print "subset ",subset
            total_divisible_subset = total_divisible_subset|subset
            #print "total_divisible_subset ",total_divisible_subset
        sum = 0

    nondivisible_subsets = sets - total_divisible_subset
    print "ans " ,nondivisible_subsets
    print len(total_divisible_subset)

k = 5
s = [770528134,663501748,384261537,800309024,103668401,538539662,385488901,101262949,557792122,46058493]
nonDivisible_subsets(k,s)
