# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении
# с использованием функции

def y(t): 
    v0 = 5       # Начальная скорость
    g = 9.81     # Ускорение свободного падения
    return v0*t - 0.5*g*t**2
	
t = 0.6      # Время
print (y(t))
t = 0.9
print (y(t))

"""
1)SyntaxError: invalid syntax
2)    g = 9.81     # Ускорение свободного падения
    ^
IndentationError: unexpected indent
3)    g = 9.81     # Ускорение свободного падения
    ^
IndentationError: unexpected indent
4) def yt): 
          ^
SyntaxError: invalid syntax
5)TypeError: y() takes 0 positional arguments but 1 was given
6)TypeError: y() missing 1 required positional argument: 't'
"""