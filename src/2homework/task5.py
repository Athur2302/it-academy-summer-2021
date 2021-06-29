n = int(input("Введите): "))
num1, num2 = (0, 1)
i = 1
while i < n:
    num1, num2 = (num2, num1 + num2)
    i += 1
    if i == n:
        print(num1)
