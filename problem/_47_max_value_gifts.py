def max_value_gifts(matrix):
    if len(matrix)==0:return None
    out =[[0 for _ in range(len(matrix)+1)] for _ in range(len(matrix[0])+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            out[i+1][j+1] = max(out[i][j+1],out[i+1][j])+matrix[i][j]
    return out[i+1][j+1]

def max_value_gifts2(matrix):
    if len(matrix)==0:return None
    out =[0 for _ in range(len(matrix[0])+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            out[j+1] = max(out[j+1],out[j])+matrix[i][j]
    return out[j+1]


if __name__ == '__main__':
    matrix = [[1,10,3,8],
              [12,2,9,6],
              [5,7,4,11],
              [3,7,16,5]
              ]
    print(max_value_gifts2(matrix))