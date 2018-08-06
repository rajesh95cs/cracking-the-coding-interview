def bomberMan(n,grid):
    grid_list = []
    for row in grid:
        grid_row = list(row.strip())
        grid_list.append(grid_row)
    #print "grid_list ",grid_list
    t = 0
    r = len(grid_list)-1
    c = len(grid_list[0])-1
    while t != n:
        bomb_coordinates = []
        count = 1
        if count == 1:
            for i in range(len(grid_list)):
                for j in range(len(grid_list[0])):
                    if grid_list[i][j] == "O":
                        bomb_coordinates.append([i,j])
        #print "bomb_coordinates ",bomb_coordinates
        count += 1
        if count == 2:
            for i in range(len(grid_list)):
                for j in range(len(grid_list[0])):
                    if grid_list[i][j] == "O":
                        continue
                    else:
                        grid_list[i][j] = "O"
            bomb_timer2 = 3            
        #print "after planting bomb ",grid
        count += 1
        if count == 3:
            for [i,j] in bomb_coordinates:
                grid_list[i][j] = "."

                if i == 0 and j == 0:
                    grid_list[i+1][j] = "."
                    grid_list[i][j+1] = "."
                if i == r and j == c :
                    grid_list[i][j-1] = "."
                    grid_list[i-1][j] = "."
                if i == r and j == 0:
                    grid_list[i-1][j] = "."
                    grid_list[i][j+1] = "."
                if i == 0 and j == c :
                    grid_list[i-1][j] = "."
                    grid_list[i+1][j] = "."
                if i == 0 and j < c and j > 0:
                    grid_list[i][j-1] = "."
                    grid_list[i][j+1] = "."
                    grid_list[i+1][j] = "."
                if i < r and i>0 and j == 0 :
                    grid_list[i+1][j] = "."
                    grid_list[i-1][j] = "."
                    grid_list[i][j+1] = "."
                if i == r and j < c and j > 0:
                    grid_list[i][j+1] = "."
                    grid_list[i][j-1] = "."
                    grid_list[i-1][j] = "."
                if j == c and i<r and i >0:
                    grid_list[i+1][j] = "."
                    grid_list[i-1][j] = "."
                    grid_list[i][j-1] = "."
                if j < c and j > 0 and i < r and i > 0:
                    grid_list[i+1][j] = "."
                    grid_list[i-1][j] = "."
                    grid_list[i][j+1] = "."
                    grid_list[i][j-1] = "."


        t += count

    grid_string = []
    for row in grid_list:
        grid_string.append("".join(row))
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
