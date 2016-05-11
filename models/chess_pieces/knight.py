from .chesspiece import ChessPiece


class Knight(ChessPiece):
    """Class to represent Knight chess piece"""
    representation = 'N'

    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        """Get all the moves that Knight is capable of"""
        return ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1))
