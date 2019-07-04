def matrix_search(mat, n):
    if len(mat) == 0:
        return -1
    l1 = len(mat)
    l2 = len(mat[0])
    i = 0
    j = l2 - 1
    while i < l1 and j >= 0:
        if mat[i][j] > n:
            j -= 1
        elif mat[i][j] == n:
            return 1
        else:
            i += 1
    return -1


if __name__ == '__main__':
    mat = [[1, 2, 4, 5, 6, 7],
           [2, 4, 5, 6, 7, 8],
           [4, 6, 8, 9, 10, 11],
           [9, 12, 15, 17, 19, 22]]
    re = matrix_search(mat, 5)
    print(re)
    re = matrix_search(mat, 3)
    print(re)
    mat = [[1, 2, 8, 0], [2, 4, 9, 12], [4, 7, 10, 13],[6, 8, 11, 15]]
    re = matrix_search(mat,5)
    print(re)
    re = matrix_search(mat,7)
    print(re)
    mat = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(matrix_search(mat,5))