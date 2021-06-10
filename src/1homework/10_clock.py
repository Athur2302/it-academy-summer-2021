# 10 строк: время, условные выражения, from..import, for..else
# от времени импорт по местному времени

activity = {8: 'Sleeping',
              9: "В пути",
              17: "Работа",
              18: "В пути",
              20: 'Еда',
              22: 'Resting'}

time_now = местное время ()
hour = time_now.tm_hour

для activity_time в отсортированном (activity.keys ()):
    если час <activity_time:
        печать (действия [activity_time])
        перерыв
еще:
    print ('Неизвестно, AFK или спит!')