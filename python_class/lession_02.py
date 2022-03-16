# 字符串操作
zo = '帅'
name = '彩虹'
print(zo, name)
str1 = 'hello word'
# 取元素
print(str1[0])
print(str1[9])
# 取多个值，切片，[2:5:2] 开始 结束 步长   包含头不包含尾
# 开始头省略    从0开始
# 结束省略      取到末尾
print(str1[2:5:2])
print(str1[-1])
print(len(str1))
print(str1[0:len(str1):2])
# 替换元素
str1 = str1.replace('word', 'tricy')
print(str1)
print(str1.index('e'))
print(str1.find('q'))
# 格式化输出
#  第一种  占位符 ：{} --传变量的地方   .format（）
name = '张小花'
age = 18
hobby = '学习'
print('''----{2}-----
name:{2}
age:{1}
hobby:{0}
'''.format(hobby, age, name))
# 运算符
# int  ->  str   : str()  转换
print(str(123) + 'abc')
# 逻辑运算符 and  or  not
# 成员运算符   in  not in
str2 = 'python'
print(str2[0])
print('y' in str2)
# name = input('请输入姓名：')
# age = input('请输入年龄：')
# gender = input('请输入性别：')
# print('''----
# 姓名：{0}
# 年龄:{1}
# 性别：{2}
# '''.format(name, age, gender))
str3 = 'python hello aaa 123123aabb'
print(str3[:6])
print('o a' in str3)
print('he' in str3)
print('ab' in str3)
print(str3.replace('python', 'lemon'))
print(str3.find('aaa'))
print(int('12') + 5)
