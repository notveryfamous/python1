# for循环
for i in range(50, 100, 2):  # 对序列进行遍历（起始，结尾，步长）
    print(i)

list1 = [1, 2, 3, 4, 5]
tuple1 = (5, 6, 7)
dict1 = {'name': '张三', 'age': 18}
set1 = {'a', 'b', 'c'}
for a in list1:
    print(a)
for b in tuple1:
    print(b)
for c in dict1:
    print(c)  # 访问字典的键
for d in dict1:
    print(dict1[d])  # 访问字典的值
for e in set1:
    print(e)