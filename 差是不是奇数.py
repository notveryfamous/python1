# 输入两个整数，若两数之差为奇数则输出，否则打印‘不是奇数’
# 一个input接受一次用户输入
number1 = int(input('请输入一个数字：'))
number2 = int(input('请输入另一个数字：'))
if (number1 - number2) % 2 != 0:
    print('奇数')
else:
    print('不是奇数', number1 - number2)