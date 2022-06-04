# Python Instructions

## Preparation

> 从https://www.python.org/downloads/ 下载最新版python，并安装  
> 从https://code.visualstudio.com/ 下载Visual Studio Code，并安装  
> 新手指南https://wiki.python.org/moin/BeginnersGuide 
> 在线文档https://docs.python.org/3/ 
> 语法https://docs.python.org/3/reference/ 


## Terminal命令

检查python版本：`$ python3 —-version` `$ python —-version` 都可以
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

## 数组



```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]

print(courses)      #返回['History', 'Math', 'Physics', 'CompSci']
print(len(courses)) #返回4
print(courses[0])   #返回History 正数第一个
print(courses[-1])  #返回CompSci 倒数第一个
print(courses[0:2]) #返回['History', 'Math'] return objects from 1st to 3rd(not include 3rd)
print(courses[:2]) #返回['History', 'Math'] return objects from 1st to 3rd(not include 3rd)
print(courses[2:]) #返回['Physics', 'CompSci'] return objects from 3rd to the last one

courses.append('Art')#向末尾添加'Art'
courses.insert(0, 'Art')#向0号位置插入'Art'
courses.insert(0, courses_2)#向0号位置插入'Art'，将返回[['Art', 'Education'], 'Math', 'Physics', 'CompSci']。整个数组都被填在0号位置
courses.extend(course_2) #向末尾添加数组内对象， 将返回['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
courses.remove('Math') #从数组里去除Math
popped = courses.pop #新建一个变量抓取将要返回的，去除的对象（从末尾开始去除）
courses.reverse()   #返回颠倒顺序的数组
courses.sort()  #返回按照字母顺序alphabetical排列
nums.sort() #返回按照升序ascending排列
courses.sort(reverse=True)  #返回颠倒字母顺序排列
nums.sort(reverse=True) #返回降序排列

#在不使用数组method不改变原数组的情况下，使用function将改变后的结果存到新变量里。
sorted_courses = sorted(courses)
print(sorted_courses)

print(max(nums))    #返回最大值
print(min(nums))    #返回最小值
print(sum(nums))    #返回总和
print(courses.index('CompSci')) #将返回这个单词在第几位
print('Art' in courses) #检查数组内有没有单词

#获得数组内的每个对象
for item in courses: #item不是built-in变量，任何变量都可以放在这。
    print(item)

for index, course in enumerate(courses, start=1): #start=1规定输出从1开始计数
    print(index, course) #将返回 序号和对象
#返回
#1 History
#2 Math
#3 Physics
#4 CompSci

#courses的内容看开头
course_str = ', '.join(courses) #join是string的method，意思是使用''内的内容来分隔join括号内的变量。将直接得到对象，而非字符串
#返回 
#History, Math, Physics, CompSci

new_list = course_str.split(', ') #将刚刚转换为单词的变量course_str转换为被', '分隔的字符串。

print(course_str)
#返回
#History - Math - Physics - CompSci

print(new_list)
#返回 
#['History', 'Math', 'Physics', 'CompSci']


```

We can not modify tuples. In programming this is called mutable and immutable.
**Lists are mutable and tuples are immutable.**

```python
#mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)
#return
#['History', 'Math', 'Physics', 'CompSci']
#['History', 'Math', 'Physics', 'CompSci']


#immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'  #

print(tuple_1)
print(tuple_2) 
#return
#('History', 'Math', 'Physics', 'CompSci')


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print('Math' in cs_courses)
#return True

print(cs_courses.intersection(art_courses))
#return{'History', 'Math'}
print(cs_courses.difference(art_courses))
#return{'Physics', 'CompSci'}
print(cs_courses.union(art_courses))
#return{'Art', 'CompSci', 'Math', 'Design', 'History', 'Physics'}


# Empty Lists
empty_list = []     #使用中括号创建
empty_list = list() #直接创建

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dictionary
empty_set = set(), set('foobar'), set(['a', 'b', 'foo'])    #不同的方法

```

## key value pair 键值对

```python
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('phone')) #get an inexistent key
#return None

print(student.get('phone'), 'Not Found') #pass the value we want as the second value
#return Not Found

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(studnet)
#return {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

del student['age']  #delete

age = student.pop('pop') #remove age from student
print(age)
#return 25

print(len(student)) #number of keys. length of student set
#return 3

print(student.keys())
#return dict_keys(['name', 'age', 'courses'])

print(student.values())
#return dict_values(['John', 25, ['Match', 'CompSci']])

print(student.items())  #loop through pairs of keys and values
#return dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])


for key, value in student.items() #loop through keys and values
    print(key, value)

```

## IF 条件句

```python
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

if language == 'Python':
    print('Language is Python')
elif language == 'Java': 
    print('Language is Java')
elif language == 'JavaScript': 
    print('Language is JavaScript')
else:
    print('No match')


user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in #'and': both needs to be true. 'or': either is true.
    print('Admin Page')
else:
    print('Bad Creds')


if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


```
 
```python
a = [1, 2, 3]
b = [1, 2 ,3]

print(a == b)
#return True，数组内容相同
print(a is b)
#return False. 两个对象都有内建的ID函数，
print(id(a))
print(id(b))
#return two strings of numbers

#如果
a = [1, 2, 3]
b = a
print(a is b)
#return Ture. b继承了a的内建的ID函数，
rint(id(a))
print(id(b))
#返回的两串ID数字串将会是相等的

#在if条件句的判断evaluate中，
# False Values: 被判断为False的condition
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

```

## Loop

```python
for num in nums:
    if num == 3:
        print('Found!')
        continue #break will stop loop
    print(num)

for i in range(1, 11):
    print(i)
#return 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 不包括最后一个数字

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
#return 0, 1, 2, 3, 4,

x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
#return 0, 1, 2, 3, 4,

#如果遇到无法停止的循环，在其循环过程中按下control+C
```

## Function