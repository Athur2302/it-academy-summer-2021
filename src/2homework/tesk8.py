# 1 задание
thickness = int(input()) #This must be an odd number
c = 'H'
width = 20
#Top Cone
for i in range(thickness):
    print((c*i).rjust (thickness-1)+c+(c*i).ljust (thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center (thickness*2)+(c*thickness).center  (thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center (thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center (thickness*2)+(c*thickness).center  (thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust  (thickness)+c+(c*(thickness-i-1)).ljust  (thickness)).rjust  (thickness*6))

# 2 задание
Пример
3
5
Выведите следующее:
8 
-2 
15

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a + b 
    d = a - b 
    q = a * b

print(c, "сумму двух чисел")
print (d , "разница двух чисел")
print (q , "произведение двух чисел")

# 3 задание
def split_and_join(line):
    a = line.split()
    lin = "-".join(a)
    return (lin)

# 4 задане 
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a // b
    d = a / b
print(c, "целочисленного деления", d , "деления с плавающей запятой")

# 5 задние
def under_attack(col, queens):
    left = right = col
    for r, c in reversed(queens):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False
