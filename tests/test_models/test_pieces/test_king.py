import unittest
from models.chessboard import ChessBoard
from models.chess_pieces.king import King


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.king = King()
        self.chess_board = ChessBoard(3, 3)

    def test_get_moves_class_method_returns_expected_moves(self):
        expected_moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                          (0, 1), (1, -1), (1, 0), (1, 1))
        self.assertEqual(self.king.get_moves((3, 3), 0, 1), expected_moves)

    def test_valid_moves_available_for_King_in_board(self):
        expected_moves = {(0, 0), (0, 1), (1, 0), (1, 1)}
        self.assertEqual(
            self.king.get_valid_moves(self.chess_board, 0, 0),
            expected_moves
        )
