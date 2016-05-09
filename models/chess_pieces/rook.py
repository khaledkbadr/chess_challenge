from itertools import chain
from .chesspiece import ChessPiece


class Rook(ChessPiece):
    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        len_x, len_y = board_dimensions
        horizontal_moves = [(row - x, 0) for row in range(len_x)]
        vertical_moves = [(0, col - y) for col in range(len_y)]
        return chain(horizontal_moves, vertical_moves)

