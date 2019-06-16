class Singleton(object):
	_list={}
	def __new__(cls,*args,**kwargs):
		if cls not in cls._list:
			cls._list[cls]=super(Singleton,cls).__new__(cls,*args,**kwargs)
		return cls._list[cls]


class A(Singleton):
	def __init__(self,a):
		super(A,self).__init__()
		self.a=a

if __name__ == '__main__':
	a=A(1)
	b=A(2)
	print(a.a,b.a)