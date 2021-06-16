a = int(input('Введите число: '))
b = a
pal = 0
while a > 0:
    digit = a % 10
    pal = pal * 10 + digit
    a = a // 10
if b == pal:
    print("Это палиндром!")
else:
    print("Это не палиндром!")