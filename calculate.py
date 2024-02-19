from base_library import *
from sympy import *
from sympy.abc import (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)            
import matplotlib.pyplot as plt

def equations(user_input, solve_for = None):
    try:
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
        return solution

    except Exception as err:
        print("an error occured") 
        print(err)

def graph(user_input, solve_for = None):
    try:
        equality = user_input.index("=")
        load()
        equivalent_value = make_equal_to(user_input, equality)
        load()
        user_input = user_input[:equality]
        load()
        equal_val = sympify(sympifiable(str(equivalent_value)))
        load()
        user_input = Eq(sympify(user_input), equal_val)
        load()
        solution = return_solved_equation(user_input, solve_for)
        load()
        return solution

    except Exception as err:
        print("an error occured") 
        print(err)


