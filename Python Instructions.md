# Python Instructions

## Preparation

> 从https://www.python.org/downloads/ 下载最新版python，并安装  
> 从https://code.visualstudio.com/ 下载Visual Studio Code，并安装  
> 新手指南https://wiki.python.org/moin/BeginnersGuide 
> 在线文档https://docs.python.org/3/ 
> 语法https://docs.python.org/3/reference/ 


## Terminal命令

检查python版本：`$ python3 —version`
进入文件夹：`$ cd 文件夹地址（简介里复制）`
打开/执行文件：`$ python3 文件名.py`

## VS Code

先在左侧extensions里搜索python，安装第一个扩展。
找个地儿新建一个文件夹，在VS里打开这个文件夹，并在VS里新建一个空文件保存为.py格式。

## Python 名词概念

text data in python is called a string 字符串
  
## Python 语法

注释comments
`#……` #The comments start with a hash character/the pound sign
**变量习惯于用小写字母lowercase组成，如有多个单词，用下划线underscore隔开。**名称尽可能具有描述性，说明性

每行不需要分号semicolon



Methods and functions are basically the same thing. Method is just a function that belong to an object

## 语句

string字符串，用单引号`''`single quote，如果文本包含单引号，则在单引号前添加反斜线`\` backslash。 例如：`'Bobby\'s World'`，或者`"Bobby’s World"`达到同样效果。使用三个双引号`"""XXX"""`将强制字符串化，包括范围内的换行。

```python
message = 'Hello World'  
message = "Kai's World"
message = """Kai's World was a good
metaverse in 2020s"""
```

`print(len(message))`, `len()` 打印变量message的长度, return 11
print(message[0]) 
print(message[0:5]) #打印第一至第六个范围内的字母
print(message[6:])  #打印第七至最后一个字母
print(message.lower())  #变成小写字母
print(message.upper())  #变成大写字母
print(message.count('l'))   #计数l再变量message中出现的次数
print(message.find('World'))    #查找World的位置，return 6，因为World从第六个开始。如果找不到，则return -1

new_message = message.replace('World', 'Universe')  #需要新变量名继承变化，原变量无法更新。
message = message.replace('World', 'Universe')  #需要重新设置变量，原变量无法自动更新改变。
print(message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome '    #使用‘+’将文本连接，但不适合处理复杂文本
message = '{}, {}. Welcome!'.format(greeting, name) #使用placeholder大括号占据空位，用format函数填充空位
message = f'{greeting}, {name.upper()}. Welcome!'   #新的长字符串表达方式，用f，并将内容填写在大括号内，不再用format函数。并且可在大括号内继续使用其他函数
print(message)

print(help(str.lower))  #学会使用print(help())查阅函数的功能和参数

