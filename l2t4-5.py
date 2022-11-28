# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Реализуйте алгоритм перемешивания списка.

import random

n = int(input('введите целое число: '))
pos1 = 0
pos2 = n - 1
list =[]
for i in range(n):
    list.append(random.randint(-n, n))
print(list)
print(list[pos1]*list[pos2])

for i in range(n):
    x1 = random.randint(0, n-1)
    x2 = random.randint(0, n-1)
    list[x1],list[x2]=list[x2],list[x1]
print(list)
