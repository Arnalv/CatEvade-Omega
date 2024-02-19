from sympy.plotting.plot import Parametric2DLineSeries
from base_library import *
from sympy import *
from sympy.plotting.plot import List2DSeries, Plot
from sympy.abc import (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)            

import numpy as np
import sys

def equations(solve_for = None):
    while True:
        try:
            user_input = str(get_input(str(sys.argv)))
            equality = user_input.index("=")
            load()
            solve_flag = make_solve_flag(user_input)
            load()
            solve_for = make_solve_for(solve_flag, user_input, solve_for)
            load()
            equivalent_value = make_equal_to(user_input, equality, solve_flag)
            load()
            user_input = user_input[:equality]
            load()
            equal_val = sympify(sympifiable(str(equivalent_value)))
            load()
            user_input = Eq(sympify(user_input), equal_val)
            load()
            solution = return_solved_equation(user_input, solve_for)
            load()
            print("|-< ", solution, "\n")

        except Exception as err:
            print("an error occured") 
            print(err)


def graph(beginning_point, distance, tallness, text = False):
    if text == True:
        import plotext as plt
    else:
        import matplotlib.pyplot as plt
    
    if beginning_point == None:
        beginning_point = 0
    if distance == None:
        distance = 10
    if tallness == None:
        tallness = 10
    while True:
        try:
            user_input = str(get_input(str(sys.argv), "y = "))
            if "show" not in user_input:
                load()
                lam_x = lambdify(x, user_input, modules=['numpy'])
                load()
                x_val = np.linspace(beginning_point, distance, tallness)
                load()
                y_val = lam_x(x_val)
                load()
                plt.plot(x_val, y_val)
            else:
                plt.show()

        except Exception as err:
            print("an error occured") 
            print(err)
            


