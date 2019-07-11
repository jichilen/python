def all_list_of_str(str1):
    def helper(str1):
        if len(str1) == 0:
            return [[]]
        result = []
        for i in range(len(str1)):
            out = helper(str1[:i]+str1[i+1:])
            for x in out:
                x.append(str1[i])
                result.append(x)
        return result
    return helper(str1)

if __name__ == '__main__':
    str1 = "abd"
    print(all_list_of_str(str1))