# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
my_list = ['a', 'b', 'c']
my_tuple = tuple(my_list)
print(my_tuple)

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
my_typle = ('a', 'b', 'c')
my_list = list(my_list)
print(my_list)

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = "a", 2, "python"
print(a, b, c)


# Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.
my_typle_1 = ([1, 2, 3],)
for i in my_typle_1[0]:
print(i)
print(len(my_typle_1))
