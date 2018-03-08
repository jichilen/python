#coding=utf-8
'''
将字符串转换成数字
"1234" 
to 
1234
'''
def fn(a,b):
	return 10*a+b
def char2num(a):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[a]
def str2num(a):
	return reduce(fn,map(char2num,a))
print str2num("1121")


print '\n'
b=int("1121")
print b