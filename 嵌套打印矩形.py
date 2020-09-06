# Python可以使用一层循环打印三角形
# i = 0
# while i < 5:
#    i += 1
#    print('*' * i)


# 总结：外循环控制行数，内循环控制列数
# 打印星星
j = 0
while j < 5:
    j += 1
    # 打印五个星星并换行
    i = 0
    while i < 5:
        i += 1
        print('*', end='   ')  # 打印一个星星不换行
    print()  # 换行
