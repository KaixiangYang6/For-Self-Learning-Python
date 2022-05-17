message = 'Hello World'
print(len(message)) # 打印变量message的长度,return 11
print(message[0])  #获得字符的单个字母
print(message[0:5]) #打印第一至第六个范围内的字母
print(message[6:])  #打印第七至最后一个字母
print(message.lower())  #变成小写字母
print(message.upper())  #变成大写字母
print(message.count('l'))   #计数l再变量message中出现的次数
print(message.find('World'))    #查找World的位置，return 6，因为World从第六个开始。如果找不到，则return -1

new_message = message.replace('World', 'Universe')  #可以用新变量名继承变化。
message = message.replace('World', 'Universe')  #需要重新定义变量，来继承改变。
print(message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome '    #使用‘+’将文本连接，但不适合处理复杂文本
message = '{}, {}. Welcome!'.format(greeting, name) #使用placeholder大括号占据空位，用format函数填充空位
message = f'{greeting}, {name.upper()}. Welcome!'   #新的长字符串表达方式，用f，并将内容填写在大括号内，不再用format函数。并且可在大括号内继续使用其他函数
print(message)

print(help(str.lower))  #学会使用print(help())查阅函数的功能和参数