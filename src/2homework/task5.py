n = input("ввод:")
a = 1
b = 1
n = int(n)
i = 0

while i < n - 2:
    sum = a + b
    b = sum
    i = i + 1
print(b)
