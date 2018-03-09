# coding=utf-8
'''
抛出错误
'''


def foo(s):
    n = int(s)
    return 10 / n


def bar(s):
    try:
        return foo(s) * 2
    except StandardError as e:
        print "error!"
        raise ValueError("input error")
    else:
        pass
    finally:
        print "finally"


def main():
    bar('0')


if __name__ == '__main__':
    main()
