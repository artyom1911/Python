'''1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0.56 -> 11'''

a = input('Введите число = ')
c = 0
if type(a) == int:
    while a > 0:
        b = a % 10
        c = b + c
        a = a // 10
        

if type(a) == float:
    while a > 0:
        b = a % 10
        c = b + c
        a = a // 10
        
print (c)
