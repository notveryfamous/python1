# continue和break
# continue：直接结束本次循环，进入下一次循环
# break：结束整个循环


year = 1
summ = 0

while year <= 20:

    print('第', year, '年到了……')

    if year == 10:
        print('今年你受伤了，彩礼就不用给了！')
        year += 1
        continue

    month = 1
    while month <= 12:
        summ += 0.1
        print('第', year, '年，第', month, '月，给1.2万彩礼，累积支付', round(summ, 2), '万')
        month += 1

    year += 1

year0 = 1
summ0 = 0


while year0 <= 20:

    print('第', year0, '年到了……')

    if year0 == 10:
        print('今年你受伤了，彩礼就不用给了！')
        year0 += 1
        break

    month0 = 1
    while month0 <= 12:
        summ0 += 0.1
        print('第', year0, '年，第', month0, '月，给1.2万彩礼，累积支付', round(summ0, 2), '万')
        month0 += 1

    year0 += 1