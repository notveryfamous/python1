# 打印从0到100的整数
i = 0
while i <= 100:
    print(i)
    i += 1

# 嵌套循环
year = 1
summ = 0

while year <= 20:

    print('第', year, '年到了……')

    month = 1
    while month <= 12:
        summ += 0.1
        print('第', year, '年，第', month, '月，给1.2万彩礼，累积支付', round(summ, 2), '万')
        month += 1

    year += 1

# print('第', year, '年，给1.2万彩礼，累积支付', round(summ, 2), '万')
