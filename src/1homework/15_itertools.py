от itertools import groupby
линии = '' '
Это
первый параграф.

Это второй.
'' '.splitlines ()
# Используйте itertools.groupby и bool для возврата групп
# последовательные строки, которые либо содержат, либо нет.
для has_chars, фрагов в groupby (lines, bool):
    если has_chars:
        print ('.join (фраги))
# ПЕЧАТИ:
# Это первый абзац.
# Это второ