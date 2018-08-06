def bomberMan(n,grid):
    grid_list = []
    for row in grid:
        grid_row = list(row.strip())
        grid_list.append(grid_row)
    #print "grid_list ",grid_list

    r = len(grid_list)-1
    c = len(grid_list[0])-1
    grid_intlist = []
    for i in range(len(grid_list)):
        row = []
        for j in range(len(grid_list[0])):
            if grid_list[i][j] == '.':
                row.append(0)
            if grid_list[i][j] == 'O':
                row.append(3)
        grid_intlist.append(row)
    #print grid_intlist
    if (n%4 == 0):
        grid_string = []
        for row in grid_intlist:
            temp =[]
            for i in row:
                if i != 0:
                    temp.append('O')

                else:
                    temp.append('.')
            grid_string.append(''.join(temp))
        print '\n'.join(grid_string)
    if n%4 == 1:
        for i in range(len(grid_intlist)):
            for j in range(len(grid_intlist[0])):
                if grid_intlist[i][j] == 0:
                    grid_intlist[i][j] = 3
                elif grid_intlist[i][j] == 3:
                    grid_intlist[i][j] -= 1
        grid_string = []
        for row in grid_intlist:
            temp =[]
            for i in row:
                if i != 0:
                    temp.append('O')

                else:
                    temp.append('.')
            grid_string.append(''.join(temp))
        print '\n'.join(grid_string)
    if n%4 == 2:
        for i in range(len(grid_intlist)):
            for j in range(len(grid_intlist[0])):
                if grid_intlist[i][j] == 0:
                    grid_intlist[i][j] = 2
                elif grid_intlist[i][j] == 3:
                    grid_intlist[i][j] -= 2
        grid_string = []
        for row in grid_intlist:
            temp =[]
            for i in row:
                if i != 0:
                    temp.append('O')

                else:
                    temp.append('.')
            grid_string.append(''.join(temp))
        print '\n'.join(grid_string)
    if n%4 == 3:
        bomb_coordinates = []
        for i in range(len(grid_intlist)):
            for j in range(len(grid_intlist[0])):
                if grid_intlist[i][j] == 3:
                    bomb_coordinates.append([i,j])
                else:
                    grid_intlist[i][j] = 1
        for [i,j] in bomb_coordinates:
            grid_intlist[i][j] = 0

            if i == 0 and j == 0 and i<r and j<c:
                grid_intlist[i+1][j] = 0
                grid_intlist[i][j+1] = 0
            if i == r and j == c :
                grid_intlist[i][j-1] = 0
                grid_intlist[i-1][j] = 0
            if i == r and j == 0 and j<c:
                grid_intlist[i-1][j] = 0
                grid_intlist[i][j+1] = 0
            if i == 0 and j == c and i<r :
                grid_intlist[i-1][j] = 0
                grid_intlist[i+1][j] = 0
            if i == 0 and j < c and j > 0:
                grid_intlist[i][j-1] = 0
                grid_intlist[i][j+1] = 0
                grid_intlist[i+1][j] = 0
            if i < r and i>0 and j == 0 :
                grid_intlist[i+1][j] = 0
                grid_intlist[i-1][j] = 0
                grid_intlist[i][j+1] = 0
            if i == r and j < c and j > 0:
                grid_intlist[i][j+1] = 0
                grid_intlist[i][j-1] = 0
                grid_intlist[i-1][j] = 0
            if j == c and i<r and i >0:
                grid_intlist[i+1][j] = 0
                grid_intlist[i-1][j] = 0
                grid_intlist[i][j-1] = 0
            if j < c and j > 0 and i < r and i > 0:
                grid_intlist[i+1][j] = 0
                grid_intlist[i-1][j] = 0
                grid_intlist[i][j+1] = 0
                grid_intlist[i][j-1] = 0
        grid_string = []
        for row in grid_intlist:
            temp =[]
            for i in row:
                if i != 0:
                    temp.append('O')

                else:
                    temp.append('.')
            grid_string.append(''.join(temp))
        print '\n'.join(grid_string)






file = open('test.txt','r')
data_s = file.readlines()
data = data_s[0].split()
r = int(data[0])
c = int(data[1])
n = int(data[2])
del data_s[0]
grid = []
for data in data_s:
    grid.append(data)

#print len(obstacles)
bomberMan(n,grid)
