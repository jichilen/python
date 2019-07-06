def pos_of_search_tree(pos):
    def helper(pos):
        if len(pos) <= 1:
            return True
        rootv = pos[-1]
        midflag = 0
        midind = 0
        for num in pos[:-1]:
            if midflag == 0:
                if num>rootv:
                    midflag = 1
                else:
                    midind += 1
            else:
                if num<rootv:
                    return False
        return helper(pos[:midind]) and helper(pos[midind:-1])
    return helper(pos)


if __name__ == '__main__':
    pos = [5,7,6,9,11,10,8]
    print(pos_of_search_tree(pos))
    pos = [5, 7, 6, 4, 11, 10, 8]
    print(pos_of_search_tree(pos))