#coding=utf-8
'''
解析xml
读取xml每一级标签中的内容
生成xml并且完成解析
提取所需要的信息
'''

from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        # pass
        print('sax:start_element:%s,attrs:%s'%(name,attrs))
    def end_elemnt(self,name):
        # pass
        print('sax:end_element:%s'% name)
    def char_data(self,text):
        if text=='python':
            print('this is what exactly i want : sax:char_data:%s' % text)

# xml=r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# xml生成，注意生成也需要严格符合xml格式，不然解析失败

L=[]
L.append(r'<?xml version="1.0"?>')
L.append(r'<ol>')
L.append(r'<li><a href="/a">python</a></li>')
L.append(r'<li><a href="/b">b</a></li>')
L.append(r'</ol>')
x=''.join(L)

handler=DefaultSaxHandler()
parser=ParserCreate()
parser.returns_unicode=True
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_elemnt
parser.CharacterDataHandler=handler.char_data
parser.Parse(x)

# print parser
