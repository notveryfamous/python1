# ASCII --> Latin1 --> Unicode
# 函数 chr 和 ord 能查看数字与字符的对应关系

print(ord('a'))
print(chr(88))
print(ord('你'))
print(chr(12371))

# 字符串转换为编码集结果 encode方法

# GBK 一个汉字两个字节
print('你'.encode('gbk'))
# UTF8 一个汉字三个字节
print('你'.encode('utf8'))

x = b'\xe4\xbd\xa0'
print(x.decode('utf8'))

# 产生乱码
y = '你好'.encode('utf8')
print(y)
print(y.decode('gbk'))