import unittest
from models.chessboard import ChessBoard
from models.chess_pieces.queen import Queen


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.queen = Queen()
        self.chess_board = ChessBoard(3, 3)

    def test_get_moves_class_method_returns_expected_moves(self):
        expected_moves = {(0, 1), (-1, 1), (0, 0),
                          (-2, 2), (2, 0), (1, 1),
                          (2, 2), (1, 0), (0, 2)}
        self.assertEqual(self.queen.get_moves((3, 3), 0, 0), expected_moves)

    def test_valid_moves_available_for_Queen_in_board(self):
        expected_moves = {(0, 1), (0, 0), (0, 2),
                          (2, 0), (2, 2), (1, 0),
                          (1, 1)}
        self.assertEqual(
            self.queen.get_valid_moves(self.chess_board, 0, 0),
            expected_moves
        )
