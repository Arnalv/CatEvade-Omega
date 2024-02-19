# CatEvade Omega
## A CLI for solving for x

this program allows to solve for x in your terminal.
currently, the only supported feature of sympy is solving equations.

## Requirements

* Python 3
* preferably a UNIX based OS

## How to use

clone this repository, then cd in.
run these commands to install the dependencies
```
pip install sympy
pip install matplotlib
pip install pygments
pip install prompt_toolkit 
```
### Equations

start the program with `python cli.py equate`
you can then run equations like this
`|-> x + 5 = g`
or solve for a particular variable with a `#` like this
`|-> x - y = h / j #x`
or you can also run the program with the `-s` flag in order to solve for a particular variable by default, like this
```
python cli.py equate -s x
|-> x + y = h
```
### Graphs
start the program with `python cli.py graph`
you can then run plots like this
`|-> y = x + 5`
or show the graph
`|-> y = show`
or you can also run the program with the `-g False`(default) flag in order to show the graph in a seperate window, or you can set `-g` to True to show the graph in the terminal
run the `-b`, `-l`, and `-t` flags to change the beginning point, length, and height/tallness respectively
