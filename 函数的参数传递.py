# 参数设定方法：顺序传入，关键词，默认参数，不定长参数


def show(name, age, sex, hobby):  # 形参
    print('我叫：', name, '，年龄：', age, '，性别：', sex, '，爱好：', hobby)


# 顺序传入
show('张三', 18, '男', '打球')  # 实参

# 关键词
show(name='张三', sex='男', age=18, hobby='打球')  # 要么使用顺序传入，要么使用关键词


# 默认参数
def show(name, age, hobby, sex='男'):
    print('我叫：', name, '，年龄：', age, '，性别：', sex, '，爱好：', hobby)


show('张三', 18, '打球')


def show(name, sex, hobby, age=22):
    print('我叫：', name, '，年龄：', age, '，性别：', sex, '，爱好：', hobby)


show(name='张三', sex='男', age=18, hobby='打球')  # 以手动填写的参数为结果


# 不定长参数
def add(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


print(add(37, 555, 6))
print(add())
print(add(37, 555, 6, 5552, 5887447))
