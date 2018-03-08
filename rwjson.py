#coding=utf-8
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
with open('Color Scheme - Default.sublime-package','rb') as f:
    # with open('111.txt', 'w') as fp:
        # fp.write(f.read(1000))
    pass


import json
import logging
#DEBUG INFO WARNING ERROR
logging.basicConfig(level=logging.DEBUG)
d=dict(name='Bob',scor=80)
logging.info(d)
logging.info(json.dumps(d))