from math import sqrt
k = int(input('Введите коэф k: '))
a1 = int(input('Введите кол-во ноликов: '))
a2 = int(input('Введите кол-во крестиков: '))

#координаты точек нужно вводить через пробел, пример: 3 6
a_0 = a_x = []
for i in range(a1):
    o = [int(x) for x in input('Введите координаты для точки для ноликов: ').split()]
    a_0 += [o]

    x = [int(x) for x in input('Введите координаты для точки для крестиков: ').split()]
    a_x += [x]

b = [int(x) for x in input('Введите координаты главной точки: ').split()]
res = []
for i in range(a1):
    x = sqrt( (b[0] - a_0[i][0])**2 + (b[1] - a_0[i][1])**2 )
    res += [[x, 0]]

for i in range(a2):
    x = sqrt( (b[0] - a_x[i][0]) ** 2 + (b[1] - a_x[i][1])**2 )
    res += [[x, 1]]
res.sort()
res = res[:k]
cnt_o = cnt_x = 0
for i in range(len(res)):
    if res[i][1] == 0: cnt_o += 1
    else: cnt_x += 1
if cnt_o > cnt_x:
    print(f'Точка {b} относится к ноликам, кол-во ближайших ноликов {cnt_o}, кол-во ближайших крестиков {cnt_x}')
else:
    print(f'Точка {b} относится к крестикам, кол-во ближайших ноликов {cnt_x}, кол-во ближайших крестиков {cnt_o}')
