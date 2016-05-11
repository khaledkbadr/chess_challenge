from .chesspiece import ChessPiece


class King(ChessPiece):
    """Class to represent King chess piece"""
    representation = 'K'

    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        """Get all the moves that King is capable of"""
        return ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1))
