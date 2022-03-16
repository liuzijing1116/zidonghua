"""
for 变量名 in 数据对象：
    子代码

range 内置函数  和循环一起使用  生成整数序列
"""
count = 0
list1 = [1, 2, 3, 4, 5, 6]
for num in list1:
    if num == 3:
        # break
        continue
    print(len(list1))
for i in range(1, 5, 1):
    print(i)
'''
函数
def 函数名():
    子代码
'''

'''
传参类型
1.按照位置传参
2.关键字传参
3.关键字传参必须在位置传参后面
'''

# 等前面的必备参数和默认参数接收完了，剩下的都给不定长参数args


# def good_job(a, b, *args, c=5):
#     sub = a + b + c
#     # for i in args:
#     #     sub += i
#     print('sub的值为：{}'.format(sub))
#     print(args)


#good_job(1, 2, 3)
#good_job(a=1, b=2, c=6)
#good_job(6, b=4, c=8)
def good_job(a, b, c=9, *args, **kwargs):
    sub = a+b+c
    print(sub)
    print(args)
    print(kwargs)
    for j in  kwargs:
       #print(kwargs.get(j))
       print(kwargs[j])
    return sub


a = good_job(0, 1, 2, 3, 8, aa=4, bb=5)
print(a)
