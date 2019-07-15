def first_num_appear_once(strs):
    dic = {}
    for i,s in enumerate(strs):
        if s in dic:
            dic.pop(s)
        else:
            dic[s] = i
    return min(list(dic.values()))

if __name__ == '__main__':
    strs="abbaccdeff"
    print(first_num_appear_once(strs))