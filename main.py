import time
import argparse
from itertools import chain
from .models.chess_pieces.queen import Queen
from .models.chess_pieces.king import King
from .models.chess_pieces.rook import Rook
from .models.chess_pieces.knight import Knight
from .models.chess_pieces.bishop import Bishop


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-x', '--columns', type=int)
    parser.add_argument('-y', '--rows', type=int)
    parser.add_argument('-q', '--queens', type=int)
    parser.add_argument('-b', '--bishops', type=int)
    parser.add_argument('-r', '--rooks', type=int)
    parser.add_argument('-n', '--knights', type=int)
    parser.add_argument('-k', '--kings', type=int)

    args = parser.parse_args()

    pieces = tuple(chain(
        [Queen] * args.queens,
        [Rook] * args.rooks,
        [Bishop] * args.bishops,
        [Knight] * args.knights,
        [King] * args.kings))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time for solving problem %s seconds' % (time.time() - start_time))
