before = float(input('请输入您的税前工资：'))
m1 = float(input('请输入社保扣除工资：'))

ss = 0  # 纳税金额
ys = before - m1 - 5000  # 应纳税所得额

if 3000 >= ys >0:
    ss = ys * 0.03 - 0
elif 12000 >= ys:
    ss = ys * 0.1 - 210
elif 25000 >= ys:
    ss = ys * 0.2 - 1410
elif 35000 >= ys:
    ss = ys * 0.25 - 2660
elif 55000 >= ys:
    ss = ys * 0.3 - 4410
elif 80000 >= ys:
    ss = ys * 0.35 - 7160
elif ys > 80000:
    ss = ys * 0.45 - 15160


print('您的应纳税金额：', ss, '到手工资：', before - m1 - ss)