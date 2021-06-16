x= list(input("Введите строку: "))
a = 0
b = 0
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in x:
    if i in english:
        if i.isupper() == True:
            a += 1
        elif i.islower() == True:
            b += 1
print(a ," больших прописных английских букв")
print(b ,"маленьких прописных английских букв")