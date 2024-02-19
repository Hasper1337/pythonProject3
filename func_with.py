from collections.abc import *


def flatten(l):  # Функция была несщядна украдена с темы: https://clck.ru/38txz5
    for j in l:
        if isinstance(j, Iterable) and not isinstance(j, (str, bytes)):
            yield from flatten(j)
        else:
            yield j


print(*list(flatten([1, [2, [3, [4, [5]]]]])), sep=" -> ", end=" -> None")  # подумать над выводом
