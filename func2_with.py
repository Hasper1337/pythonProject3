from functools import *


@lru_cache(None)
def for_x(n):
    if n == 0 or n == 1:
        return 1
    else:
        return for_x(n - 2) + (for_x(n - 1) / (2 ** (n - 1)))


print("Результат вычислений ->", for_x(5))
