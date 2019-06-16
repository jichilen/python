# coding=utf-8
'''
读取写入程序
使用json存储实例
'''
# try:
#     f=open('iterclass.py','r')
#     print f.read()
# except Exception as e:
#     raise e
# finally:
#     f.close()

# 读写文件
with open('Color Scheme - Default.sublime-package', 'rb') as f:
    # with open('111.txt', 'w') as fp:
    # fp.write(f.read(1000))
    pass

# 序列化
import json
import logging

# DEBUG INFO WARNING ERROR
logging.basicConfig(level = logging.DEBUG)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
logging.info(json.dumps(s, default = student2dict))
try:
    logging.info(json.dumps(s))
except Exception as e:
    raise e


# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook = dict2student))
