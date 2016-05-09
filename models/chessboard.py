class ChessBoard:
    def __init__(self, m, n):
        self.squares = [[None for _ in range(m)] for _ in range(n)]
