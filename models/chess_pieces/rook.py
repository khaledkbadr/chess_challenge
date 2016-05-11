from itertools import chain
from .chesspiece import ChessPiece


class Rook(ChessPiece):
    """Class to represent Rook chess piece"""
    representation = 'R'

    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        """Get all the moves that Rook is capable of"""
        len_x, len_y = board_dimensions
        horizontal_moves = [(row - x, 0) for row in range(len_x)]
        vertical_moves = [(0, col - y) for col in range(len_y)]
        return tuple(chain(horizontal_moves, vertical_moves))
