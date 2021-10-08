# 作者：童鼎

# 知识点_用户输入

# 用户输入方法： input()
# 回顾上节课知识：登录系统（while循环、input输入）
# 本节：打印（print）输出的一般方法

name = input("name: ")
age = input("age: ")
job = input("job: ")
salary = input("salary: ")


# 注释来写内容存到字符串中
# 知识点1：字符串拼接用+ 让打印结果更加直观

info1 = '''-----INFO '''+name+'''-----'''+'''
age: '''+age+'''
job: '''+job+'''
salary: '''+salary
print(info1)

# 知识点2：占位符将 + 省略
# %s占位符可以将 + 省略
info2 = '''-----INFO %s -----
name:%s
age:%s
job: %s
salary: %s''' %(name,name,age,job,salary)
print(info2)

# 知识点3: .format() 比起%s 更适合较多变量的打印，不需要考量顺序和出现次数
# 例如 ： url 的拼接（http:// + 域名 + endpoint）
info3 = '''-----INFO {HTML_name} -----
name:{HTML_name}
age:{HTML_age}
job: {HTML_job}
salary: {HTML_salary}''' .format(HTML_job=job,HTML_age=age,HTML_name=name,HTML_salary=salary)


print(info3)

# 假定你要求用户以2021-10-27 格式输入
user_input_time = "2021-10-27"
# 字符串拆分，方法 split 拆分完结果是一个 列表
print(user_input_time.split('-'))
print(user_input_time.split('-')[0])

# 知识点_列表

names = "xxxyl,wkkkk,shasha"
# print(names[1])
names_list = ["xxxyl","wkkkk","shasha"]
password_list = [123,124,322]
age_list = [23,23,42]
# ...
# 列表的嵌套
info_list = [["xxxyl",123,23],["wkkkk,1234,23"]]

print(names_list[0])
print(password_list[0])
print(age_list[0])
print(info_list[0])


names2 = ["Mike","Mary","Jan"]
# 知识点 slices（切片） 数值是指values 在list中的位置

# 1.正向取值
# 列表取值“：”右边的值取不到 例如[1:3] 3这个位置取不到
print(names2[1:3])
# 如果 左侧值为 0 即从0开始取值，0也可以省略不写
print(names2[:2])

# 2.反向取值
# list 取值“：”右边的值取不到 例如[-3:-1] -1这个位置取不到
# 注意：取到最后一个值 不用写0 省略即可
print(names2[-3:-1])

num = [1,2,3,4,5,6]
# 对比 range

print(list(range(10)))
print(num[2:4])