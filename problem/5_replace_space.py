def replace_space(str):
    out = ''
    for s in str:
        if s == ' ':
            out += "%20"
        else:
            out += s
    return out




if __name__ == '__main__':
    str= "We are happy."
    print(replace_space(str))
