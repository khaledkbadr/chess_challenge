class ChessBoard:
    def __init__(self, m, n):
        self.len_x = m
        self.len_y = n
        self.squares = [[None for _ in range(m)] for _ in range(n)]
        self.threatened_squares = set()
        self.valid_squares = set((x, y) for x in range(m) for y in range(n))
        self.num_pieces = 0  # Number of pieces placed on the board
