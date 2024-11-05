'''
Rotate by 90 degree
Given a square mat[][]. The task is to rotate it by 90 degrees in clockwise direction without using any extra space.
'''
def rotate(mat): 
    n = len(mat)

    # Perform Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each row
    for row in mat:
        row.reverse()
