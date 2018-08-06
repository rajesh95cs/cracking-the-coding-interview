
l = len(A)
   w = len(A[0])
   max_height = 0
   planar_connections = 0
   vertical_connections = 0
   no_of_cubes = 0
   for i in range(l):
       for j in range(w):
           no_of_cubes += A[i][j]
           if A[i][j] > 0:
               vertical_connections += (A[i][j] - 1)
           if max_height < A[i][j]:
               max_height = A[i][j]
   for k in range(max_height):
       for i in range(l):
           for j in range(w):
               if A[i][j] > 0:
                   if j+1 < w:
                       if A[i][j+1] > 0:
                           planar_connections += 1
                   if i+1 < l:
                       if A[i+1][j] > 0:
                           planar_connections += 1
                   A[i][j] -= 1

   Area = 6*(no_of_cubes) - (2*(planar_connections+vertical_connections))
   return Area
