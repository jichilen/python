#coding=utf-8
'''
从html中提取信息
'''
from HTMLParser import HTMLParser
from htmlentitydefs  import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print '<%s>%s'%(tag,attrs)
        pass
    def handle_endtag(self, tag):
        pass
        # print '<%s>'%tag
    def handle_startendtag(self, tag, attrs):
        pass
        # print 'se<%s>'%tag
    def handle_data(self, data):
        pass
        # print data
    def handle_comment(self, data):
        pass
        # print '<!-- -->'
    def handle_entityref(self, name):
        # print '&%s'%name
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass

parser=MyHTMLParser()
with open('./events.html','r')as f:
    for line in f:
        parser.feed(line)

