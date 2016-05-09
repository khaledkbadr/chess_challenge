import time
import argparse
from itertools import chain
from models.chessboard import ChessBoard
from models.chess_pieces.queen import Queen
from models.chess_pieces.king import King
from models.chess_pieces.rook import Rook
from models.chess_pieces.knight import Knight
from models.chess_pieces.bishop import Bishop
from models.helpers import place_piece_on_board


def start_boards(size_x, size_y, first_piece):
    """Generate a board for each placement and place the first_piece in it"""
    for x in range(size_x):
        for y in range(size_y):
            board = ChessBoard(size_x, size_y)
            place_piece_on_board(board, first_piece, x, y)
            yield board  # We use yield to save memory


def solve(len_x, len_y, pieces):
    """Returns all configuration for the chess challenge"""
    first_piece, other_pieces = pieces[0], pieces[1:]
    solutions = set()

    for board in start_boards(len_x, len_y, first_piece):
        pass
    return solutions


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-x', '--columns', type=int)
    parser.add_argument('-y', '--rows', type=int)
    parser.add_argument('-q', '--queens', type=int, default=0)
    parser.add_argument('-b', '--bishops', type=int, default=0)
    parser.add_argument('-r', '--rooks', type=int, default=0)
    parser.add_argument('-n', '--knights', type=int, default=0)
    parser.add_argument('-k', '--kings', type=int, default=0)

    args = parser.parse_args()

    pieces = tuple(chain(
        [Queen] * args.queens,
        [Rook] * args.rooks,
        [Bishop] * args.bishops,
        [Knight] * args.knights,
        [King] * args.kings))

    results = solve(args.columns, args.rows, pieces)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time for solving problem %s seconds' % (time.time() - start_time))
