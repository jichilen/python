# coding=utf-8
'''
使用sys.argv来记录输入参数
'''

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print "hello world"
    elif len(args) == 2:
        print "hello,%s" % args[1]
    else:
        print "too many args"


def main():
    test()


if __name__ == '__main__':
    main()
