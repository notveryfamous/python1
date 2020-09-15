def foo(ele):
    return ele['age']
    # print('ele = {}'.format(ele))


# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]
nums.sort()
print(nums)

# sorted内置函数，不会改变原有列表，会生成一个新的有序的列表
nums = [4, 8, 2, 1, 7, 6]
x = sorted(nums)
print(x)

ints = (5, 9, 2, 1, 3, 8, 7, 4)
y = sorted(ints)
print(y)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]
# 字典与字典没有可比性
# 缺少比较条件
# 需要传入参数key(函数)
students.sort(key=foo)  # 在sort实现时，内部调用了foo方法，并且传入了一个参数，参数就是列表中的元素
print(students)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]
students.sort(key=lambda ele: ele['score'])
print(students)