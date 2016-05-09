from .chesspiece import ChessPiece


class Knight(ChessPiece):
    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        return ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1))
