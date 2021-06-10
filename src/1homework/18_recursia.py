BOARD_SIZE = 8
def under_attack (col, ферзей):
    слева = справа = столбец для r, c в обратном порядке (ферзи):
    влево, вправо = влево - 1, вправо + 1

    если c in (left, col, right):
        вернуть True
    вернуть ложь

def решить (n):
    если n == 0:
        возвращаться [[]]

    small_solutions = решить (n - 1)

    return [решение + [(n, i + 1)]
        для i в диапазоне (BOARD_SIZE)
            для решения в small_solutions
                если не under_attack (i + 1, решение)]
для ответа в решении (BOARD_SIZE):
    печать (ответ)