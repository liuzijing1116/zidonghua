# 常用数据类型
# 转换  list() tuple() set()
# 1.列表 list []  元素可以是任意的数据类型  int float bool str list    列表元素可以增加 修改  删除
list1 = [1, 2.1, True, '看', [1, 2, 3]]  # 空列表
print(list1)
print(list1[4])
print(list1[0:list1.index('看')])
print(list1[4][0])
# 增加
list1.append('a')  # 默认追加元素到末尾
list1.insert(3, '六')
list1.extend(['q', 'w', 'e'])
print(list1)
# 删除
list1.pop(0)  # 可以指定[0] 索引
list1.remove('a')  # 指定元素本身删除
# list1.clear()  # 清除所有元素
print(list1)
# 修改
list1[1] = '5'
print(list1)

# 元组 () tuple   元组的元素不可以被改变
tuple1 = (1, 2.1, True, '看', [1, 2, 3], 6)
list2 = list(tuple1)
list2.remove(6)
tuple2 = tuple(list2)
print(tuple2)

# 字典 dict {}
# key value 键值对  存储数据属性用到
# key不能是 list和dict  可以是str；不能重复，唯一性。
# value可以是任意类型
# 不能用索引取值
dict1 = {'name': 'a', 'height': '180', 'weight': '85'}
print(dict1['height'])
print(dict1.get('weight'))
dict1['age'] = 18 # 如果key不存在，则会添加key value
dict1.update({'gender': 'man', 'name': '学习'})  # update 字典添加多个键值对，如果添加已经存在的key，会替换值
print(dict1)
# dict1.pop('age')
# print(len(dict1))

# 集合 {} 单个 无序 元素不可以重复   使用场景为去重
list3 = [1, 2, 3, 4, 5, 6, 1, 2]
set1 = set(list3)
list4 = list(set1)
print(list4)
'''
控制流  判断 循环
判断
if 条件:
    子代码
elif 条件:
    子代码
else:
    子代码
'''
a = [1, 2, '6', 'summer']
if 'i' in a:
    print("123")
else:
    print('456')

dict_1 = {'class_id': 45, 'num': 20}
if dict_1.get('num') > 5:
    print(dict_1.get('num'))

list_1 = ['方方', '花花', '荷花', '小草', 'qq', '换蓝']


