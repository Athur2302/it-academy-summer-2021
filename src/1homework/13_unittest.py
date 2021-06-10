# импорт unittest
def median (пул):
    копия = отсортировано (пул)
    size = len (копия)
    если размер% 2 == 1:
        вернуть копию [int ((size - 1) / 2)]
    еще:
        return (copy [int (size / 2-1)] + copy [int (size / 2)]) / 2
класс TestMedian (unittest.TestCase):
    def testMedian (сам):
        self.assertEqual (медиана ([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
если __name__ == '__main__':
    unittest.main ()