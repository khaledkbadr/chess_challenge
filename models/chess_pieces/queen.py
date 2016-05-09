from itertools import chain
from .chesspiece import ChessPiece
from .rook import Rook
from .bishop import Bishop


class Queen(ChessPiece):
    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        return chain(Rook.get_moves(board_dimensions, x, y),
                     Bishop.get_moves(board_dimensions, x, y))
