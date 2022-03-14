#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#导入安装的requests库，使用import语句实现
# noinspection PyUnresolvedReferences
import requests
#导入yagmail库，使用import语句实现,yagmail 可以简单的来实现自动发邮件功能
# noinspection PyUnresolvedReferences
import yagmail

#需要requests库中的get方法，用于请求网站的访问。requests.get('url')
#requests.get即是调用requests库的get方法，小括号()中填写需要访问的网站地址
print(requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京'))    #返回200的状态码表示访问成功

#用requests.get方法读取到的原始城市天气信息进行保存并使用json方法处理原始数据，之后再赋值给新的变量使用
data = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
weather = data.json()

print(weather)

#练习：读取南京城市天气信息，并正确的将变量通过json方法处理成Python可以处理的数据，最后使用print()输出信息
data = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=南京')
weathernj = data.json()

print(weathernj)


print("————————————分割线————————————")


##城市天气信息查询
#查询城市名
city = weather['data']['city']
print(city)
#查询昨日最高温度
yesterday_high = weather['data']['yesterday']['high']
print(yesterday_high)
#查询当日最低温度
today_low = weather['data']['forecast'][0]['low']
print(today_low)


print("————————————分割线————————————")


#练习：读取南京当天城市天气信息，并通过print()输出第二天的风力信息
citynj = weathernj['data']['city']
print(citynj)
today_typenj = weathernj['data']['forecast'][0]['type']
print(today_typenj)
fenglinj = weathernj['data']['forecast'][1]['fengli']
print(fenglinj)


print("————————————分割线————————————")


##自动插入天气数据
#格式化字符串的方法是使用format()方法，先在需要格式化的字符串内部用大括号{}在需要变量打印的位置占位，之后在字符串后用format(变量1，变量2，变量……)依次替换字符串内的占位符
name='Tom'
type='晴'
print('Hello {}，今日天气{}。'.format(name,type))

#练习：读取当天南京的最高温度、最低温度、感冒预警信息，并使用格式化字符输出
citynj = weathernj['data']['city']
typenj = weathernj['data']['forecast'][0]['type']
highnj = weathernj['data']['forecast'][0]['high']
lownj = weathernj['data']['forecast'][0]['low']
forecastnj = weathernj['data']['ganmao']
print('今日{}天气：{}，气温：{} ~ {}，{}'.format(citynj, typenj, highnj, lownj, forecastnj))


print("————————————分割线————————————")


##邮件发送天气预报
#导入库，然后初始化对象
yag = yagmail.SMTP(user='757426958@qq.com', password='oegpwpqotrcvbbeg',host='smtp.qq.com')
#发送邮件，目标是自己，随便写一个标题和内容即可，后续可自行编辑内容
#yag.send(to = '757426958@qq.com',subject ='测试邮件标题',contents = "用python发送邮件")