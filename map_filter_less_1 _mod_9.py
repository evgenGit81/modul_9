# -*- coding: utf-8 -*-
def kvadrat(element):
    """Возведение в квадрат числа"""
    return element ** 2
def nechet(element_2):
    """Возвращает нечетные числа"""
    if (element_2 % 2) != 0:
        return element_2


list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
list_2 = list(map(kvadrat, list_))
list_3 = list(filter(nechet, list_2))
print(list_3)
