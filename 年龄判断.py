# 根据输入年龄判断是否成年，若超出范围（0到150岁）则打印‘这不是人’
age = int(input('请输入您的年龄：'))
if 0 <= age <= 150:
    if age < 18:
        print('未成年')
    else:
        print('成年')
# 年龄在正常范围
else:
    print('这不是人！')