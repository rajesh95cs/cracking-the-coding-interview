fname = "Test_case.txt"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
        print(len(line))
print count
