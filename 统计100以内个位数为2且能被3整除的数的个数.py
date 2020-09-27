# 关于数学
count = 0  # 定义一个变量来表示个数
for i in range(1, 101):
    if i % 10 == 2 and i % 3 == 0:
        count += 1  # 只要发现符合的数字，就把计数器增加1
print(count)