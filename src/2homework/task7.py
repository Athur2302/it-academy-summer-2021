# три стороны треугольника
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
if a + b > c and b + c > b and c + a > b:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    print("треугольник существует", s)
else:
    print("не существует")
