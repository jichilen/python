def solution(matrix, target):
    rs = len(matrix)
    if rs == 0: return False
    cs = len(matrix[0])
    visited = [[0 for _ in range(cs)] for _ in range(rs)]
    def path_in_matrix(matrix, r, c, rs, cs, target,visited):
        if len(target)==0:
            return True
        if r < 0 or c < 0 or r >= rs or c >= cs:
            return False
        if matrix[r][c]!=target[0] or visited[r][c]==1 :
            return False
        visited[r][c]=1
        if path_in_matrix(matrix, r+1, c, rs, cs, target[1:],visited) or \
            path_in_matrix(matrix, r-1, c, rs, cs, target[1:],visited) or \
            path_in_matrix(matrix, r, c+1, rs, cs, target[1:],visited) or \
            path_in_matrix(matrix, r, c-1, rs, cs, target[1:],visited):
            return True
        visited[r][c]=0
        return False
    for i in range(rs):
        for j in range(cs):
            if path_in_matrix(matrix, i, j, rs, cs, target,visited):
                return True
    return False


if __name__ == '__main__':
    matrix = [
        ['a', 'b', 't', 'g'],
        ['c', 'f', 'c', 's'],
        ['j', 'd', 'e', 'h']
    ]
    matrix = [
        ['a','b','c','d','e']
    ]
    matrix = [
        ['a'], ['b'], ['c'], ['d'], ['e']
    ]
    target = 'bfce'
    target = 'abfb'
    target = 'acfbtcede'
    target = 'cba'
    print(solution(matrix, target))
