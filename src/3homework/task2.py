# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
str_ = "bcd"
dano_list = []
for i in str_:
    dano_list.append("a" + i)
for i in str_:
    dano_list.append("b" + i)
print(dano_list)

# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
dano_list_1 = dano_list[::2]
print(dano_list_1)

# Используйте генератор списков чтобы получить следующий:
# ['1a', '2a', '3a', '4a']
dano_list_2 = []
for i in range(1, 5):
    dano_list_2.append(str(i) + "a")
print(dano_list_2)

# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его
print(dano_list_2.pop(1))

# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
# списке этого элемента не было
dano_list_3 = dano_list_2[:]
dano_list_3.insert(1, "2a")

print(dano_list_3)
