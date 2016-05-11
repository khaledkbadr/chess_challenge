Problem
=======

The problem is to find all unique configurations of a set of normal chess pieces on
a chess board with dimensions M×N where none of the pieces is in a position to take any of the
others. Assume the colour of the piece does not matter, and that there are no pawns among the
pieces.

Write a program which takes as input:
The dimensions of the board: M, N.
The number of pieces of each type (King, Queen, Bishop, Rook and Knight) to try and
place on the board.
As output, the program should list all the unique configurations to the console for which all of
the pieces can be placed on the board without threatening each other.
When returning your solution, please provide with your answer the total number of unique
configurations for a 7×7 board with 2 Kings, 2 Queens, 2 Bishops and 1 Knight.


Results
=======

To get help on program, just run it as following:

```
> python main.py
usage: main.py [-h] [-x COLUMNS] [-y ROWS] [-q QUEENS] [-b BISHOPS]
                [-r ROOKS] [-n KNIGHTS] [-k KINGS]

board dimensions:
  -x COLUMNS, --columns COLUMNS
                        columns
  -y ROWS, --rows ROWS  rows

pieces on board:
  -q QUEENS, --queens QUEENS
                        number of Queens
  -b BISHOPS, --bishops BISHOPS
                        number of Bishops
  -r ROOKS, --rooks ROOKS
                        number of Rook
  -n KNIGHTS, --knights KNIGHTS
                        number of Knights
  -k KINGS, --kings KINGS
                        number of Kings
```

Examples
========
```
> python main.py --rows=7 --columns=7 --queens=2 --kings=2 --bishops=2 --knights=1

3063828 unique configurations found (only 10 is printed)
Time for solving problem 2413.5026681423187256 seconds

```

Note: Board printing is omitted in the README
