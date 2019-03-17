#Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки
#сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

a = int(input());
b = int(input());
c = int(input());
if a >= b:
    if b >= c :
        print(a);
        print(c);
        print(b);
    elif a > c:
        print(a);
        print(b);
        print(c);
    else:
        print(c);
        print(b);
        print(a);
else:
    if a >= c :
        print(b);
        print(c);
        print(a);
    elif b>c:
        print(b);
        print(a);
        print(c);
    else:
        print(c);
        print(a);
        print(b);
