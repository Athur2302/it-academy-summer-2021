# импорт csv
# необходимо определить функцию cmp в Python 3
def cmp (a, b):
    return (a> b) - (a <b)

# записываем данные об акциях в виде значений, разделенных запятыми
с open ('stocks.csv', 'w', newline = '') как stocksFileW:
    Writer = csv.writer (stocksFileW)
    writer.writerows ([
        ['GOOG', 'Google, Inc.', 505,24, 0,47, 0,09],
        ['YHOO', 'Yahoo! Inc. ', 27,38, 0,33, 1,22],
        [CNET, CNET Networks, Inc., 8.62, -0.13, -1.4901]
    ])

# читать данные по акциям, распечатывать сообщения о статусе
с open ('stocks.csv', 'r') как stocksFile:
    stocks = csv.reader (stocksFile)

    status_labels = {-1: "вниз", 0: "без изменений", 1: "вверх"}
    для тикера, имени, цены, изменения, процента на акциях:
        status = status_labels [cmp (float (изменение), 0,0)]
        print ('% s - это% s (% .2f)'% (имя, статус, число с плавающей запятой (pct)))