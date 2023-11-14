#!/usr/bin/python3
#!/usr/bin/python3
"""
2d Rotate matrix module
"""

def rotate_2d_matrix(matrix):
    """
    2d Rotate matrix function
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
