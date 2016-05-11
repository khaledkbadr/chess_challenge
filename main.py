import time
import argparse
from itertools import chain
import copy
from models.chessboard import ChessBoard
from models.chess_pieces.queen import Queen
from models.chess_pieces.king import King
from models.chess_pieces.rook import Rook
from models.chess_pieces.knight import Knight
from models.chess_pieces.bishop import Bishop
from models.helpers import place_piece_on_board, pretty_print_board


def start_boards(size_x, size_y, first_piece):
    """Generate a board for each placement and place the first_piece in it"""
    for x in range(size_x):
        for y in range(size_y):
            board = ChessBoard(size_x, size_y)
            place_piece_on_board(board, first_piece, x, y)
            yield board  # We use yield to save memory


def valid_boards(board, pieces, pieces_count):
    """Yield boards that has successful configuration for pieces"""
    valid_boards = {board}
    for piece in pieces:
        _valid_boards, valid_boards = valid_boards, set()
        for n, board in enumerate(_valid_boards):
            for square in board.valid_squares - board.threatened_squares:
                _board = copy.copy(board)
                _placed = place_piece_on_board(_board, piece, *square)
                if not _placed:
                    continue
                if _board.num_pieces == pieces_count:
                    yield _board
                else:
                    valid_boards.add(_board)


def solve(len_x, len_y, pieces):
    """Returns all configuration for the chess challenge"""
    first_piece, other_pieces = pieces[0], pieces[1:]
    solutions = set()

    for board in start_boards(len_x, len_y, first_piece):
        solutions.update(set(
            str(s)
            for s in valid_boards(board, other_pieces, len(pieces))))
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
    print(len(results))
    for n, board in enumerate(results):
        pass
        # print(pretty_print_board(args.columns, board))
if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time for solving problem %s seconds' % (time.time() - start_time))
