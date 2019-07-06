def print_matrix_clockwise(matrix):
    rows = len(matrix)
    if rows == 0:
        return
    cows = len(matrix[0])
    out = []
    for outiter in range(0,min(rows,cows),2):
        bourder = outiter//2
        for upi in range(bourder,cows-bourder):
            out.append(matrix[bourder][upi])
        for righti in range(1+bourder,rows-bourder):
            out.append(matrix[righti][cows-bourder-1])
        if rows-bourder-1 == bourder or cows-bourder-1 == bourder:
            break
        for downi in range(cows-bourder-2,bourder-1,-1):
            out.append(matrix[rows-bourder-1][downi])
        for lefti in range(rows-bourder-2,bourder,-1):
            out.append(matrix[lefti][bourder])
    print(out)

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print_matrix_clockwise(matrix)
    matrix = [
        [1, 2],
        [5, 6],
        [9, 10],
        [13, 14]
    ]
    print_matrix_clockwise(matrix)
    matrix = [
        [1],
        [5],
        [9],
        [13]
    ]
    print_matrix_clockwise(matrix)
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print_matrix_clockwise(matrix)
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    print_matrix_clockwise(matrix)
    matrix = [
        [1, 2, 3, 4],
    ]
    print_matrix_clockwise(matrix)
