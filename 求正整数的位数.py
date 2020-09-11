# 不可使用判断字符串长度的方式
num = int(input('请输入一个正整数：'))
count = 0  # 表示个数
while True:
    count += 1
    num //= 10
    if num == 0:
        break
print(count)