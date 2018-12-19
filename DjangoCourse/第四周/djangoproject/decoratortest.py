"""
Python的装饰器用法:
1.python中函数名的特殊含义；
2.python中闭包的概念
3.装饰器的用法；(装饰器就是通过闭包来实现的)
"""
#第一部分:函数名
#python中函数名，也可以理解为一个变量，可以将其赋值给其他变量；同时也可以修改这个函数名变量；
# def a():
#     print('a函数')
# b=a
# b()
# def a1(num):
#     print('num=',num)
#     num()#num()其实就是a()
# #将a这个函数名，传递到a1这个函数中
# a1(a)
#
# def a2():
#     print('==')
#     #函数名变量作为返回值使用
#     def a3():
#         print('这是一个私有函数a3')
#     return a3
#
# #调用a2函数得到一个新的函数a3
# res=a2()
# res()#等价于a3()

#第二部分:闭包
#闭包的概念:如果一个函数内部，包裹着有另外一个或多个函数，那么这个内部的私有函数就称为闭包；
#闭包的特点:可以保存一个函数内部的局部变量信息不被释放，暂时停留在内存当中，方便后续函数的调用。
#函数内部的局部变量,由于在函数外部不能使用，所以当函数执行完毕以后，这个局部变量就会从内存中销毁。
# def sum(value):
#     num=1
#     num+=value
#     print('num=',num)

# for x in range(4):
#     sum(1)

#如何保证上述num值累加?
#1.将num声明成全局变量；
#缺点:a>全局变量在程序运行期间一直会占用内存；等程序结束的时候这个全局变量才会销毁。b>容易造成全局变量名冲突。
#2.使用闭包;闭包的重要作用就是管理函数内部的局部变量。

# def sum(value):
#     num=1
#     #wrapper()就是一个闭包，这个闭包引用了外部函数sum的两个局部变量num和value
#     def wrapper():
#         #如果在闭包内部修改外部函数变量的值，闭包内部需要使用nonlocal来修饰这个变量，如果只是在闭包内引用外部变量的值，不需要使用nonlocal。
#         nonlocal num
#         num+=value
#         print(num)
#     return wrapper
# res=sum(1)#res就是wrapper。
# for x in range(4):
#     res()

#第三部分：装饰器。
#作用：在不改变原有函数结构(包括函数名、参数、函数体)的基础上，给某一个函数添加额外的功能。
import time

#result_time就是一个装饰器，参数func_name就是用来接收被装饰的函数，必须声明。
# def result_time(func_name):
#     def wrapper():
#         start_time=time.time()
#         func_name()
#         end_time=time.time()
#         print('执行时间',end_time-start_time)
#     return wrapper
# #@result_time就相当于执行了wrapper=result_time(show)
# @result_time
# def show():
#     print('show函数开始执行')
#     time.sleep(2)
#     print('show函数执行结束')
#
#
# # wrapper=result_time(show)
# # wrapper()
# #show()就相当于执行了 wrapper(),就相当于调用了wrapper()函数
# show()

#理解装饰器：其实就是将装饰器的函数(show)传到装饰器(func_name)内部，然后装饰器内部调用show。而此时的def show()这个show变成了wrapper这个闭包。所以，装饰器函数，最根本的目的就是为了调用闭包函数。

#如何通过装饰器传递参数？
def show_html(name):
    #show_html函数就是用来接收@show_html传递的参数
    def wrapper1(func_name):
        #func_name还是用于接收被修饰的函数
        def wrapper():
            print('当前展示的页面是:',name)
            func_name()
        return wrapper
    return wrapper1
@show_html('首页')
def get_method():
    print('函数执行完毕')

get_method()

#装饰器的普通调用方式:
# wrapper1=show_html('首页')
# wrapper=wrapper1(get_method)
# wrapper()
