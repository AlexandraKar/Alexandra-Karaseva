print('Введите три числа:')
a = int(input())
b = int(input())
c = int(input())
s = 0
if a + b == c:
    print('Число',c,'равно сумме первых двух чисел.')
else:
    print('Число',c,'не равно сумме первых двух чисел.')
if a * c + b == 0:
    x = c
    print('Число',c,'является решением линейного уравнения a * x + b = 0, где a - первое число, b - второе число.')
else:
    print('Число',c,'не является решением линейного уравнения a * x + b = 0, где a - первое число, b - второе число.')