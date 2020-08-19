import random

# 1.简单if判断
money = 66
if money > 100:
    print('可以买宝马啦')
    print('好开心')
else:
    print('还是骑我的破自行车吧')

# 2.elif多条件判断
money = random.randint(0, 150)
if money >= 100:
    print('可以买宝马啦')
    print('好开心')
    print(money)
elif 100 > money >= 50:
    print('可以买丰田了')
    print('还可以')
    print(money)
elif 50 > money >= 20:
    print('可以买二手车了')
    print('啊这')
    print(money)
else:
    print('破自行车再修修吧')
    print('发财是不可能的')
    print(money)

# 3.嵌套if
# money0 = random.randint(0, 100)
# money1 = random.randint(10, 60)
money0 = int(input('请输入您的银行存款（万）：'))
money1 = int(input('请输入您的贷款额度（万）：'))
if money0 >= 100:
    print('可以买宝马啦')
    print('好开心')
    if money1 >= 50:
        print('可以买宝马740')
        print(money0 + money1 + '万元')
    elif money1 >= 30:
        print('可以买宝马520')
        print(money0 + money1 + '万元')
    elif money1 >= 20:
        print('可以买宝马320')
        print(money0 + money1 + '万元')
    else:
        print('还是去二手市场逛逛吧')
        print(money0 + money1 + '万元')
elif 100 > money0 >= 50:
    print('可以买丰田了')
    print('还可以')
    print(money0)
elif 50 > money0 >= 20:
    print('可以买二手车了')
    print('啊这')
    print(money0)
else:
    print('破自行车再修修吧')
    print('发财是不可能的')
    print(money0)