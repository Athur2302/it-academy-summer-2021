a = (input("ввод:"))
q = a.split()
t = ''
for x, y in (",", ""), ("-", ""), ("!", ""), ("?", ""), (".", ""), (":", ""):
    a = a.replace(x, y)
for i in q:
    if len(i) > len(t):
        t = i
print(t)
