import time

card1 = '1001'
pwd1 = '123456'
ban1 = 10000

card2 = '1002'
pwd2 = '123456'
ban2 = 10000

card3 = '1003'
pwd3 = '123456'
ban3 = 10000

print('欢迎来到Python银行')

error_times = 0

while True:
    card = input('请输入银行卡号：')
    pwd = input('请输入密码：')

    ban = 0

    if card == card1 and pwd == pwd1:
        ban = ban1

    elif card == card2 and pwd == pwd2:
        ban = ban2

    elif card == card3 and pwd == pwd3:
        ban = ban3

    else:
        error_times += 1
        if error_times >= 3:
            print('您已经3次输入错误，联系银行柜台')
            time.sleep(3)
            break

        else:
            print('卡号密码输入错误，请重新输入')
            time.sleep(1.5)
            continue

    while True:
        num = input('请输入要办理的业务（01.存款 02.取款 03.退卡）：')
        if num == '01':
            inn = float(input('请输入存款金额：'))
            if inn <= 0:
                print('存款金额请大于0')
                time.sleep(1.5)
                continue

            else:
                ban += inn
                print('存款成功！存入：', inn, '元，余额：', ban, '元')

        elif num == '02':
            out = float(input('请输入取款金额：'))
            if out <= 0:
                print('取款金额请大于0')
                time.sleep(1.5)
                continue

            elif out > ban:
                print('余额不足，快去赚钱！')
                time.sleep(1.5)
                continue

            else:
                ban -= out
                print('取款成功！取出：', out, '元，余额：', ban, '元')

        elif num == '03':
            print('请收好卡片，欢迎下次再来！')
            time.sleep(2.5)
            break

        else:
            print('输入有误！')
            time.sleep(1.5)
            continue