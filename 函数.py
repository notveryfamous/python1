"""
函数的基本格式
def square(x):
    s = x * x
    return s

def为关键字
square()为函数名
x为参数
s = x * x为函数主体
return为关键字，意思是返回
s为返回的变量
"""


def f1(a):  # 定义了一个函数
    print(a, '函数f1被执行了')


f1('666,')


def add(a, b, c, d):
    e = a + b + c + d
    return e


print('结果为：', add(14, 545, 656, 44))


def zzj(fruit):
    if fruit == '苹果' or fruit == '梨' or fruit == '桃子':
        print('正在榨汁！')
        print('两分钟后......')
        zhi = '一杯' + fruit + '汁'
        return zhi
    else:
        print('榨汁机要坏了！')


guozhi = zzj('石头')

print(guozhi)