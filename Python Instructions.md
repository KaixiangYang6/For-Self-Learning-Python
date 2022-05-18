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
  
## Python Syntax

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

获取变量所代表的字符串内的字符

```python
print(message[0]) #将变量变为数组格式，返回字符串的单个字母
print(message[0:5]) #打印第一至第六个范围内的字母
print(message[6:])  #打印第七至最后一个字母
```

对strings的method命令

```python
print(message.lower())  #变成小写字母
print(message.upper())  #变成大写字母
print(message.count('l'))   #计算字母`l`在变量message中出现的次数
print(message.find('World'))    #查找World的位置，return 6，因为World从第六个开始。如果找不到，则return -1
```

原变量发生变化的时候，需要再次定义一遍去继承它的变化。如下：

```python
new_message = message.replace('World', 'Universe')  #需要新变量名继承变化，原变量无法更新。
message = message.replace('World', 'Universe')  #需要重新设置变量，原变量.method无法直接使用。
print(message)
```

使用`'+'`将文本连接，但不适合处理长字符串

```python
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome '    #使用'+'将文本连接，但不适合长字符串。
```

大括号用来占位，后面的变量将按照顺序补充到位置上。`f'{变量} {变量.method}!'`是比较推荐的长字符方法。

```python
message = '{}, {}. Welcome!'.format(greeting, name) #使用大括号占位，用format填充空位
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
```


使用dir和help查找使用方法。
```python
name = 'Michael'
print(dir(name)) #show all of the attributes and methods that we have access to that variable.
print(help(str)) #show info of methods of 'str' class
print(help(str.lower)) #show info of lower method
```

`type()` 将会返回变量的数据类型

```python
num = 3
print(type(num))
```


```python
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2    不想要十分位decimal，只要整数
# Exponent:       3 ** 2    幂
# Modulus:        3 % 2     取余数
# n +=1;  n *= 2

print(3 * (2 + 1))  #括号的作用和数学中一样
print(abs(-3))      #绝对值
print(round(3.75, 1))  #对数字进行四舍五入，按照指定的位数。Round a number to a given precision in decimal digits


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

print(3 != 2) # return True
print(3 <= 2) # return False

```

**将字符整数化**

```python
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
```