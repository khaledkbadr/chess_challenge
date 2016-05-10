from abc import ABCMeta, abstractmethod
from ..helpers import square_on_board


class ChessPiece(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def get_moves(cls, board_dimensions, x, y):
        pass

    @classmethod
    def get_valid_moves(cls, board, x, y):
        if (x, y) in board.threatened_squares:
            return
        moves = [(x, y)]
        board_size = (board.len_x, board.len_y)
        for delta_x, delta_y in cls.get_moves(board_size, x, y):
            move = x + delta_x, y + delta_y
            if square_on_board(board_size, *move):
                if move in board.valid_squares:
                    moves.append(move)
                else:
                    return
        return moves
