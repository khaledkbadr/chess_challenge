import unittest
from models.chessboard import ChessBoard
from models.chess_pieces.knight import Knight


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()
        self.chess_board = ChessBoard(7, 7)

    def test_get_moves_class_method_returns_expected_moves(self):
        expected_moves = ((-2, -1), (-2, 1), (-1, -2),
                          (-1, 2), (1, -2), (1, 2),
                          (2, -1), (2, 1))
        self.assertEqual(self.knight.get_moves((7, 7), 0, 0), expected_moves)

    def test_valid_moves_available_for_Knight_in_board(self):
        expected_moves = {(1, 2), (0, 0), (2, 1)}
        self.assertEqual(
            self.knight.get_valid_moves(self.chess_board, 0, 0),
            expected_moves
        )
