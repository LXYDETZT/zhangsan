'''

print('哈哈',2333,2.333)
print('哈哈'+'嘻嘻') #字符串的拼接，但是只能相同数据类型，不过整数和小数可以一起
print('哈哈'*3) 
print(((1+2)*100-99)/2)
print(2>3)
print(4>3)

#变量和赋值-开始
#浪晋说变量必须是小写字母！为什么大写也没问题
name='张三'            #把张三这个值赋值给了a这个变量
print(name)
#变量和赋值-结束


a=input('请输入：')
print(a)

a=input('请输入：')
b=input('请输入：')
print('input获取的内容：',a+b)

#数据格式的转换-开始
print(type('哈哈'))
print(type(2333))
print(type(2.333))
print(type(True))
print(type(()))
print(type([]))
print(type({}))

print(type('123'))
print(type(int('123')))

a=int(input())
b=int(input())
print(a+b)
#数据格式的转换-结束

a='caeriovouviuolefv'
print(len(a))

a=len(input('请输入：'))
b=len(input('请输入：'))
print('两段字符串总长度为：',a+b)


#元组，下标（从0开始编号）-开始
a=(1,2,'哈哈','哈哈','嘻嘻',True,False)     #()里可以输入所有的数据类型
print(a)
print(a[4])
print(a[-1])

print(a.index('嘻嘻'))     #index用于查找数据的下标
print(a.index('哈哈'))     #index就近查找原则

print(a.count('哈哈'))     #count用于统计某个数据的数量
print(a.count(1))
print(a.count(2))
print(a.count('嘻嘻'))
print(a.count(True))
print(a.count(False))
#元组，下标（从0开始编号）-结束

#二维元组-开始
a=(1,2,'哈哈','哈哈','嘻嘻',True,False)     #()里可以输入所有的数据类型
b=(a,'哈哈','嘻嘻')   #b里有3个值，a是个整体一个值
c=(b,'哈哈','嘻嘻')
print(a)
print(b)
print(c)
print(b[0])
print(b[0][5])
print(c[0])
#二维元组-结束

#二维数组-切片-开始
a=(1,2,'哈哈','哈哈','嘻嘻',True,False)
print(a[0:4])          #左闭右开，不写或者超出都表示到边界
print(a[:4])
print(a[0:10])
print(a[0:])
#二维数组-切片-结束
'''
#数组-开始             元组和数组的区别在于元组写好后不可以修改，但是数组可以修改
a=[1,2,'哈哈','哈哈','嘻嘻',True,False]
print(a[6])
a.append('append1')
a.append('append2')
a.insert(2,'insert')
print(a)
b=a.pop(0)     #剪切
print(a)
print(b)
c=a.pop(0)
print(a)
print(c)
print(b+c)
#数组-结束