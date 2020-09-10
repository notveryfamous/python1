# for循环输出0到100的奇数
for i in range(0, 101):
    if i % 2 != 0:  # 奇数才打印
        print(i)

    if i % 2 == 0:  # 偶数不打印
        continue
    print(i)

for i in range(0, 101, 2):  # 修改步长
    print(i)
