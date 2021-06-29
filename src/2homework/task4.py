x = list(input("Введите строку: "))
a = 0
b = 0
for i in x:
    if i.isupper():
        a += 1
    elif i.islower():
        b += 1
print(a, "больших прописных английских букв")
print(b, "маленьких прописных английских букв")
