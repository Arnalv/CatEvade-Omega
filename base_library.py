import prompt_toolkit
import os 
import time

from sympy import *
from sympy.abc import *

from prompt_toolkit import PromptSession, prompt
from pygments.lexers.apl import APLLexer
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.styles import get_style_by_name
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import merge_styles
from prompt_toolkit.history import FileHistory

operators = ["+", "-", "*", "/", "^"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 't', "u", "v", "w", "x", "y", "z" ]

styles = style_from_pygments_cls(get_style_by_name('github-dark'))

menu_style = Style.from_dict({
    'completion-menu.completion': 'bg:#0088ff #0000ff',
    'completion-menu.completion.current': 'bg:#00ffff #000000',
    'scrollbar.button': 'bg:#ffffff',
    'scrollbar.background': 'bg:#88aaaa',
})

completer = WordCompleter(["0", "1", "2", "3", "5", "6", "7", "8", "9", "a", 
"b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
"s", 't', "u", "v", "w", "x", "y", "z", "+", "-", "*", "/", "^", "%", "=", "#", "clear", "quit", "show"], 
ignore_case=True)

style = merge_styles([
    styles,
    menu_style
])


hist_file = open(".history", "w")
hist_file.write("")
hist_file.close()

def get_input(command = "python cli.py equate", concat_val = ""):
    session = PromptSession(completer=completer, lexer=PygmentsLexer(APLLexer), style=style, history=FileHistory('.history'))
    user_input = session.prompt("|-> " + concat_val)
    if "quit" in user_input:
        quit()
    elif "clear" in user_input:
        os.system('cls' if os.name == 'nt' else 'clear')
        restart(command)
    else:
        return user_input

def sympifiable(Expr):
    returned_list = ""
    for i in Expr:
        if i in digits or i in operators or i in alphabet:
            returned_list += str(i)
    return str(returned_list)

def graphable(Expr):
    returned_list = ""
    for i in Expr:
        if i in digits or i in operators or i in ["x", "y"]:
            returned_list += str(i)
    return str(returned_list)

def make_equal_to(user_input, equality, solve_flag = None):
    equivalent_value = []
    if solve_flag == None:
        for i in user_input[equality:]:
            equivalent_value.append(i)
    else:
        for i in user_input[equality:solve_flag]:
            equivalent_value.append(i)
    return equivalent_value

def return_solved_equation(user_input, solve_for):
    if solve_for == None:
        return solve(user_input)
    else:
        return solve(user_input, solve_for)

def restart(command):
    while 1:
        os.system("python " + command.replace("[", "").replace("]", "").replace(",", ""))
        time.sleep(0.2)
        quit()

def load():
    print("|")

def make_solve_flag(user_input):
    try:
        return user_input.index("#")
    except:
        return None

def make_solve_for(solve_flag, user_input, solve_for):
    if solve_flag != None:
        return sympify(sympifiable(user_input[solve_flag + 1]))
    else:
        return solve_for