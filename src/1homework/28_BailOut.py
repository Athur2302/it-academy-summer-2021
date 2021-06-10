BOARD_SIZE = 8
класс BailOut (Исключение):
    проходить

def validate (королевы):
    left = right = col = королевы [-1]
    для r в обратном порядке (ферзи [: - 1]):
        влево, вправо = влево-1, вправо + 1
        если r in (left, col, right):
            поднять BailOut

def add_queen (королевы):
    для i в диапазоне (BOARD_SIZE):
        test_queens = королевы + [я]
        пытаться:
            проверить (test_queens)
            если len (test_queens) == BOARD_SIZE:
                вернуть test_queens
            еще:
                вернуть add_queen (test_queens)
        кроме BailOut:
            проходить
    поднять BailOut

королевы = add_queen ([])
печать (королевы)
print ("\ n" .join ("." * q + "Q" + "." * (BOARD_SIZE-q-1) для q в ферзях))