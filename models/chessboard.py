from .helpers import empty_copy


class ChessBoard:
    def __init__(self, m, n):
        self.len_x = m
        self.len_y = n
        self.squares = [[None for _ in range(m)] for _ in range(n)]
        self.threatened_squares = set()
        self.valid_squares = set((x, y) for x in range(m) for y in range(n))
        self.num_pieces = 0  # Number of pieces placed on the board

    def __copy__(self):
        new_board = empty_copy(self)
        new_board.len_x = self.len_x
        new_board.len_y = self.len_y
        new_board.valid_squares = self.valid_squares.copy()
        new_board.threatened_squares = self.threatened_squares.copy()
        new_board.squares = [x[:] for x in self.squares]
        new_board.num_pieces = self.num_pieces
        return new_board

    def __str__(self):
        return ''.join([''.join([c or '.' for c in r]) for r in self.squares])
