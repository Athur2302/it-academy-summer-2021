# 8 строк: аргументы командной строки, обработка исключений
# Эта программа складывает целые числа, которые были переданы в качестве аргументов в командной строке
import sys
пытаться:
    total = sum (int (arg) для arg в sys.argv [1:])
    print ('сумма =', всего)
кроме ValueError:
    print ('Укажите целочисленные аргументы')