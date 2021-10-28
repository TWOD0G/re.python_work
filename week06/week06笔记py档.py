# 作者 ： 童鼎

names_str = "molakesi,babatuosi,baerzebu"
names_list = ["molakesi","babatuosi","baerzebu"]

print(names_str[0:12:2]) #切片

# 1关于列表的增加方法
# 1.1append()
names = ["Mike","Mary","Jan","Jack"]
# append() 圆括号的内容是 对象（比较大的一个范围，python中一切皆是对象）
# append() 新增在末尾
names.append("timem00n")
names.append("tex")
print('names:')
print(names)

# 1.2 insert() 指定位置新增数据
names.insert(2,"text") #第一个参数的数据类型为int，确定插入的位置，第二个参数为str，师新增的数据
print(names)

#1.3 extend() 合并两个列表
names_list.extend(names)#a.extend(b) 将b列表合并至a列表
print('names_list:')
print(names_list)

# 2.删除
# 2.1 remove() 的操作应该先做查询，判断元素value是否存在？
names.remove("timem00n")
print('使用remove()方法后的names:')
print(names)

# 2.2 pop() 在使用pop()之前，要先了解list的长度？清楚删除的索引位置?
# 要先了解list的长度？seq 一般方法 len()
#pop与remove的区别：pop通过确定数据的索引值来删除数据，remove通过确定列表中第一个数据的值来删除数据。
print(len(names))
print('names：', names)
names.pop(2)
print('删除序列2后的names:',names)

#3 索引：index()
print('index()方法的返回值：',names.index('Jan'))#参数为列表中的value，返回结果为列表的索引（排序）



#4 清楚数据：clear()
print(names.clear())#使用clear后清空列表中的所有数值


#5 统计：counet()
names_count = ['time','next','time','last','last','last','last']
print('列表数值为：',names_count)
print('将count()参数设为last的返回值',names_count.count('last'))#统计count输入参数在该列表中总共出现的次数

#5 copy()
names1 = ['at','as','ab']
names2 = names1
names3 = names1.copy()
names1.pop(1)
print('names1',names1)
print('names2',names2)
print('names3',names3)
#从中可以看出，赋值为浅层拷贝，names2直接引用了names1对象，names2会随着names1的更改而更改，names3则是深拷贝，创建了一个独立于names1的列表