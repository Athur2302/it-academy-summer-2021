# FizzBuzz 
# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 
# 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

spi_ok = []

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        spi_ok.append("FizzBuzz")
    elif i % 3 == 0:
        spi_ok.append("Fizz")
    elif i % 5 == 0:
        spi_ok.append("Buzz")
    else:
        spi_ok.append(i)

print(spi_ok)