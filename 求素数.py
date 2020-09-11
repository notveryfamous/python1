for i in range(101, 201):  # i=103 2~102
    for j in range(2, i):  # range(2, 103)
        if i % j == 0:  # i除以某个数除尽了，i是合数
            # print(i, '是合数')
            break  # break放在内循环中，用于结束内循环
    else:
        # for...else语句：当循环中的break没有被执行的时候，就会执行else
        print(i, '是质数')