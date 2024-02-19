import argparse
from calculate import *
from base_library import *
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help = "values: equate, graph")
    parser.add_argument("-s", "--solve-for", help = "[equate] solve for a particular variable", type=str, default=None)
    parser.add_argument("-b", "--begin-at-point", help = "[graph] make the graph begin at a point", type=int)
    parser.add_argument("-l", "--length", help = "[graph] make the graph end at a certain point", type=int)
    parser.add_argument("-t", "--tallness", help = "[graph] make the graph a certain height", type=int)
    parser.add_argument("-g", "--graph-type", help = "[graph] make the graph in the trminal if True", type=bool, default=False)
    args = parser.parse_args()


    if args.function == "equate":
        equations(args.solve_for)

    if args.function == "graph":
        graph(args.begin_at_point, args.length, args.tallness, args.graph_type)

if __name__ == '__main__':
    main()