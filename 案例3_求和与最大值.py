# 求1到100的和
summ0 = 0

for x in range(101):
    summ0 += x
print(summ0)


# 求1到100的偶数和
summ1 = 0

for y in range(0, 101, 2):
    summ1 += y
print(summ1)


# 求1到100的奇数和
summ2 = 0

for z in range(1, 101, 2):
    summ1 += y
print(summ2)


# 求出列表中的最大值
numbers = [36, 258525, 4455856, 5664, 588, 201522]

maxx = 0

for max_numbers in range(0, len(numbers) - 1):
    if numbers[max_numbers + 1] >= maxx:
        maxx = numbers[max_numbers + 1]
print(maxx)