# 9 строк: открытие файлов
# сделайте отступ в коде Python, чтобы поместить его в электронное письмо импортный глобус
# glob поддерживает расширения имени пути в стиле Unix


python_files = glob.glob ('*. py')
для имени_файла в отсортированном (python_files):
    print ('------' + имя_файла)
    с открытым (имя_файла) как f:
        для строки в f:
            печать ('' + line.rstrip ())
    Распечатать()