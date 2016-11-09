# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении
#1) Привет NameError: name 'Привет' is not defined
v0 = 5       #Начальная скорость 
#2,3)SyntaxError: invalid syntax Если убрать # перед Начальная или = после v0
g = 9.81     # Ускорение свободного падения
t = 0.6      # Время

y = v0*t - (1/2)*g*t**2

print(y)# 4)NameError: name 'pint' is not defined если убрать r
#5) 3.0 если заменить вычисление у на y = v0*t
#6)NameError: name 'x' is not defined если поставить print(x) вместо print(y)
#7) Ответ не изменится, если 0.5 заменить на 1/2