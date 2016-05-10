from .chesspiece import ChessPiece


class King(ChessPiece):
    representation = 'K'

    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        return ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1))
