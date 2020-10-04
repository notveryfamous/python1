nums = [6, 5, 3, 1, 8, 7, 2, 4]
# 调用列表的 sort 方法，可以直接对列表进行排序
# sort直接对原有列表进行排序
nums.sort()
print(nums)
nums.sort(reverse=True)  # 反转
print(nums)

# 内置函数sorted，不会改变原有列表，而是生成一个新的有序列表
x = sorted(nums)
print(nums)
print(x)

names = ['zhangsan', 'lisi', 'wangwu']
names.reverse()
print(names)

names = ['zhangsan', 'lisi', 'wangwu']
print(names[::-1])