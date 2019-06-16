# def funout(*args,**kwargs):
#     print(*args)
#     print(hasattr(kwargs,'k'))
#     def func(fun):
#         def funcin(*args,**kawargs):
#             print(kwargs)
#             print("decorate")
#             return fun(*args,**kawargs)
#         return funcin
#     return func
#
# @funout(2,3,k=2)
# def add_m(a,b):
#     return a+b
#
# print(add_m(1,2))
#
# class Test:
#     name="asdf"
#
# a=Test()
# b=Test()
# b.name="fff"
# print(a.name)
# print(b.name)
