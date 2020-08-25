import time

while 1 == 1:
    print('欢迎来到快递系统')

    weight = int(input('请输入重量（千克）：'))
    num = input('请输入地点编号（01.其他 02.东三省/宁夏/青岛/海南 03.新疆/西藏 04.港澳台/国外）：')

    prize = 0

    if weight >= 3:
        if num == '01':
            prize = 10 + 5 * (weight - 3)
        elif num == '02':
            prize = 12 + 10 * (weight - 3)
        elif num == '03':
            prize = 20 + 20 * (weight - 3)
        elif num == '04':
            prize = 'error'
            print('请联系总公司！')
        else:
            print('输入错误')
    elif 3 > weight > 0:
        if num == '01':
            prize = 10
        elif num == '02':
            prize = 12
        elif num == '03':
            prize = 20
        elif num == '04':
            prize = 'error'
            print('不接受寄件，抱歉！')
        else:
            print('输入错误')
    else:
        print('输入错误')

    print('您好，此件包裹价格为', prize, '元！')
    time.sleep(5)