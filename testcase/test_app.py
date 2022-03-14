#!/usr/bin/python
# -*- coding: UTF-8 -*-

# # 定义函数
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")



# def test1(str):
#     print(str)
#     return
# test1('hhhhhhhh')
# test1(1+2+3+4+5)



# def ChangeInt(a):
#     a=10
# b=2
# ChangeInt(b)
# print(b)



#格式化字符串
# print('Hello,%s.I am %d years old.' % ('everyone', 16))
# print('Hello,{}.I am {} years old.'.format('everyone', 16))
# print('growth rate:%d %%' % 7)
# print('growth rate:{} %'.format(7))



# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)



# 可写函数说明
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("Name: ", name)
#     print("Age ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="miki")


# def info(name,age,address):
#     "打印任何传入的字符串"
#     print('Name:',name)
#     print('Age:',age)
#     print('Address:',address)
#     return
# info(name='xiaoxi',age='18',address='南京市雨花台区')


# 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("Name: ", name)
#     print("Age ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="miki")
# printinfo(name="miki")


# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)


# iii={'a':1, 'b':2, 'c':3, 'b':4}
# print(len(iii))
# print(iii)
# print(iii['b'])


# aaa={'a':11,'b':22}
# aaa['c']= 33    #添加新的键值对
# aaa['a']=7      #修改键值对
# del aaa['c']    #删除键是'c'的键值对（字典元素）
# print('a' in aaa)    #通过in判断key是否存在
# print("字典值 : %s" % aaa.keys())    #以列表返回一个字典所有的键



# tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
# print("字典值 : %s" % tinydict.items())
# print('字典值 ：{}'.format(tinydict.items()))
# # 遍历字典列表
# for key, values in tinydict.items():
#     print(key, values)


#遍历列表
# a=[1,2,'ab',4,'kkk']
# for aa in a:
#     print(aa)
#遍历字典
# b={'a':1,'b':2,'c':'ab','d':4,'e':'kkk'}
# for bb in b.items():
#     print(bb)
# print(b.get('e'))    #通过dict提供的get()方法，如果key存在，可以返回自己指定的value
# print(b.get('f'))    #通过dict提供的get()方法，如果key不存在，可以返回None
#遍历元组
# c=(1,2,'ab',4,'kkk')
# for cc in c:
#     print(cc)
#遍历集合
# d={1,2,'ab',4,'kkk'}
# for dd in d:
#     print(dd)


# l=[1,2,3,4,5,6,7]
# for i in range(len(l)):
#     print(i,l[i])

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


# n=0
# while n<10:
#     n=n+1
#     if n % 2==0:
#         continue
#     print(n)
#
# sum=0
# for x in range(11):
#     sum=sum+x
# print(sum)

#计算100以内所有奇数之和
# sum=0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)




##练习：1.在控制台输入1~7；2.随机的数字每个数字对应星期几；3.如果输入的不是1~7，提示输入错误
# 方法一：
# a=input('请输入1~7任意数字：')
# b=int(a)
# dic='星期一星期二星期三星期四星期五星期六星期日'
# if b<=0 and b>7:
#     print('输入错误')
# else:
#     num=(b-1)*3
#     print(dic[num:num+3])    #字符串截取

#方法二：
# num=int(input('请输入1~7任意数字：'))
# list=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
# if num in (1,2,3,4,5,6,7):
#     days=list[int(num)-1]
#     print(days)
# else:
#     print('输入错误')

#方法三：
# week='星期一星期二星期三星期四星期五星期六星期日'
# n=int(input('请输入星期几，例如1-7：'
#             ''))
# if n not in (1,2,3,4,5,6,7):
#     print('输入错误')
# else:
#     pos = (n-1)*3
#     weekAbbrev = week[pos:pos+3]        #字符串截取
#     print('您输入的星期是：'+weekAbbrev)

#方法四：
# while True:
#     try:
#         s=int(input('请输入1~7任意数字:'))
#         list=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#         if s<=0:
#             print('输入错误')
#         else:
#             date=list[s-1]
#             print(date)
#             break
#     except:
#         print('输入错误')

#方法五：
# dic={1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六',7:'星期日'}
# i=int(input('输入一个1~7之间的数：'))
# # print('今天是{}'.format(dic[i]))
# if i>=1 and i<=7:
#     print('今天是{}'.format(dic[i]),'输入正确')
# else:
#     print('输入错误')

#方法六
# x=int(input('输入1~7之间随机一个数字：'))
# week=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
# if x>=1 and x<=7:
#     date=week[x-1]
#     print('今天是',date)
# else:
#     print('输入错误')

x=int(input('输入1~7之间随机的数：'))

if x>=1 and x<=7:
    print('今日是星期{}'.format(x))
else:
    print('输入错误')