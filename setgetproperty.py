# coding=utf-8
'''
使用装饰器
简化setter getter书写
'''


class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if value < 0:
            print "input error"
            return -1
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


def main():
    a = Student()
    a.birth = 1995
    try:
        print a.birth
        print a.age
        a.age = 1
    except Exception as e:
        raise e
    else:
        pass


if __name__ == '__main__':
    main()
