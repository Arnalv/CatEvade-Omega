import argparse
from calculate import *
from base_library import *
import sys

parser = argparse.ArgumentParser()
parser.add_argument("function", help = "values: equate, graph")
parser.add_argument("-s", "--solve-for", help = "solve for a particular variable", type=str)
args = parser.parse_args()

while True:
    if args.function == "equate":
        if args.solve_for:
            print("|-<", equations(get_input(str(sys.argv)), args.solve_for))
            print("|_______________________________\n")
        else:

            print("|-< " + str(equations(get_input(str(sys.argv)))))
            print("\n")
    if args.function == "graph":
        if args.solve_for:

            print(graph(get_input(str(sys.argv)), args.solve_for))
        else:
            print(graph(get_input(str(sys.argv))))
