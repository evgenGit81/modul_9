# -*- coding: utf-8 -*-
def is_prime(func):
    """Определяет число простое или составное"""
    def wrapper(*args, **kwaegs):
        rst = func(*args, **kwaegs)
        if (rst != 1) and (rst % 1) == 0 and (rst % rst) == 0 and ((rst % 2) != 0) and ((rst % 3) != 0):
            print("Простое")
        else:
            print("Составное")
        return rst
    return wrapper

@is_prime
def sum_three(a=int, b=int, c=int):
    """Расчитывает сумму трех натуральных чисел"""
    result = a + b + c
    return result

result = sum_three(2, 3, 6)
print(result)
