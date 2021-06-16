a = (input("Введите строку: "))
b =[]
for i in a:
    if i not in b:
        if i != " ":
            b.append(i)
print ("".join(b))

