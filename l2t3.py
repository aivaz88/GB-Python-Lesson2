# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input('Введите любое число: '))
dict = {i: round((1+1/i)**i, 2) for i in range(1, num + 1)}
print(dict)
print(sum(dict.values()))   