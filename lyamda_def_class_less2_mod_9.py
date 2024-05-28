# -*- coding: utf-8 -*-
"""Фабрика функций"""
def calcul(cond):
    """Расчетная фабрика"""
    if cond == 1:
        def cub_quad_xy_summ_razn(data_y, data_x):
            return data_y ** 3, data_x ** 3

    elif cond == 2:
        def cub_quad_xy_summ_razn(data_y, data_x):
            return data_y ** 2, data_x ** 2

    elif cond == 3:
        def cub_quad_xy_summ_razn(data_y, data_x):
            return data_y + data_x

    else:
        def cub_quad_xy_summ_razn(data_y, data_x):
            return data_y - data_x


    return cub_quad_xy_summ_razn

b = [1, 2, 3, 4]
data_y = [12, 12, 12, 4]
data_x = [3, 6, 5, 6]
i = 0
for i in range(len(b)):
    func = calcul(b[i])
    result1 = map(func, data_y, data_x)
    print(list(result1))

""" Lyamda - фунлция"""
x = 5
resultik = lambda x: x ** 2
print(f"Лямбдя функция для - {x} в квадрате = ", resultik(x))

def quadrat(x):
    return x ** 2
print("def - функция для квадрата X - ", quadrat(x))

"""Класс для площади прямоугольника"""
class Rect:
    """"""
    def __init__(self, a):
        self.a = a
    def __call__(self, b):
        return self.a * b


square = Rect(5)
print("Площадь прямоугольника равна: ", square(7.5))