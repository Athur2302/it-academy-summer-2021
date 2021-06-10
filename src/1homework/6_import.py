# 6 строк: импорт, регулярные выражения
импорт ре
для test_string в ['555-1212', 'ILL-EGAL']:
    если re.match (r '^ \ d {3} - \ d {4} $', test_string):
        print (test_string, 'действительный местный номер телефона в США')
    еще:
        print (test_string, 'отклонено')