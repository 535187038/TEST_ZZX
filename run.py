import random


# a=random.random()
# print(a)
# b=random.randint(1,100)
# print(b)

# a="hjklmasdfg"
# print(a[2])

# a = ["a", "d", "m", "g"]
# a.append("r")
# print(a)
# a.extend()
# print(a)

# dict ={"name":"小明","pwd":"123456"}
#
# dict["name"]="小华"
# # print(dict)
# # dict.get()
# dict.items()
# print(dict)

# dict={"user":"小明","pwd":"123456"}
# name=input("请输入你的姓名：")
# pwd=input("请输入你的密码：")
# if name==dict.get("user"):
#         if pwd==dict.get("pwd"):
#             print("密码正确")
#         else:
#             print("密码错误")
# else:
#     print("账户错误")

# def sum_demo(x, y):
#     for _ in range(2):
#         x += 1
#         y += 1
#         result = x + y
#     return result
#
#
# if __name__ == '__main__':
#     result = sum_demo(1, 1)
#     print(result)

# def add():
#     a =100
#     b =200
#     c = a+b
#     d = b-a
#     return c,d,a
#
# if  __name__=='__main__':
#     res=add()
#     print(res)
#     a,b,c=res
#     print(a)
#     print(b)
#     print(c)


# def outer():
#     local = 2
#
#     def inner():
#         return local
#
#     return inner
# fn = outer()
# print(fn())

# def foo(bar=[]):
#   bar.append('hello')
#   return bar
# print(foo())


# def add (a,*args,**kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
# # 将参数进行打包，注意：函数名后面直接接括号和参数
# # add(11,22,33,44)
# # 拆包的步骤
# # 给一个变量进行传入参数
# tu = (11,22,33,44)
# # 将tu当做一个参数传入，所以只会有一个参数进行接收
# add(tu)
# # 加上*/**可以将参数进行拆包
# add(*tu)
import sys
print(sys.argv)
print(sys.argv[0])
# print(sys.platform)
# print(sys.version)
