#function to set an entire row or column to 0 when an element in an mXn matrix
#is 0.here the input var[[1,2,0,4],[2,0,5,3],[1,4,2,6]]iable 2D_matrx is list of lists
def matrx(_matrx):
#here row and col variables are used as flag variables to check whether the
#elements which was already set to 0 is not visited again
    row = [0]*len(_matrx)
    col = [0]*len(_matrx[0])
#loop through the matrix to find  elements which are 0s and flag them using
#the variables row and column by setting 1
    for i in range(0,len(_matrx)):
        for j in range(0,len(_matrx[0])):
            if _matrx[i][j] == 0:
                row[i] = 1
                col[j] = 1
#loop through the array row ,check whether the ith row is set as 0
    for i in range(len(row)):
#if the condition is satisfied then call the function nullyfy to set 0s in the
#corresponding places
        if row[i] == 1 :
            _matrx = nullyfy_row(_matrx,i)
#same iternation is done using col as variable
    for j in range(len(col)):
        if col[j] == 1 :
            _matrx = nullyfy_col(_matrx,j)
#print the matrix
    print _matrx


#function nullyfy defined to set 0s in required places in the matrix through
#iternation
def nullyfy_row(_matrx,row):
    for i in range(len(_matrx[0])):
         _matrx[row][i] = 0
    return _matrx

def nullyfy_col(_matrx,col):
    for i in range(len(_matrx)):
         _matrx[i][col] = 0
    return _matrx

_matrx = [[1,2,0,4],[2,0,5,3],[1,4,2,6]]
matrx(_matrx)
