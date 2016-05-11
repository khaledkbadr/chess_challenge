from itertools import chain
from .chesspiece import ChessPiece
from .rook import Rook
from .bishop import Bishop


class Queen(ChessPiece):
    """Class to represent Queen chess piece"""
    representation = 'Q'

    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        """Get all the moves that Queen is capable of"""
        return set(chain(Rook.get_moves(board_dimensions, x, y),
                         Bishop.get_moves(board_dimensions, x, y)))
