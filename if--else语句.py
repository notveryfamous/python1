# 1.简单if判断
money = 66
if money > 100:
    print('可以买宝马啦')
    print('好开心')
else:
    print('还是骑我的破自行车吧')

# 2.elif多条件判断
import random

a = random.randint(0, 150)
money = a
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
elif 20 > money:
    print('破自行车再修修吧')
    print('发财是不可能的')
    print(money)