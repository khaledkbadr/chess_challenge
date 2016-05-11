from .chesspiece import ChessPiece


class Bishop(ChessPiece):
    """Class to represent Bishop chess piece"""
    representation = 'B'

    @classmethod
    def get_moves(cls, board_dimensions, x, y):
        """Get all the moves that Bishop is capable of"""
        len_x, len_y = board_dimensions
        moves = set()
        for row in range(len_y):
            delta = abs(y - row)
            moves.add((delta * -1, row - y))
            moves.add((delta, row - y))
        return moves
