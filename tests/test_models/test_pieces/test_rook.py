import unittest
from models.chessboard import ChessBoard
from models.chess_pieces.rook import Rook


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.rook = Rook()
        self.chess_board = ChessBoard(3, 3)

    def test_get_moves_class_method_returns_expected_moves(self):
        expected_moves = ((0, 0), (1, 0), (2, 0), (0, -1), (0, 0), (0, 1))
        self.assertEqual(self.rook.get_moves((3, 3), 0, 1), expected_moves)

    def test_valid_moves_available_for_Rook_in_board(self):
        expected_moves = {(0, 1), (2, 0), (1, 0), (0, 0), (0, 2)}
        self.assertEqual(
            self.rook.get_valid_moves(self.chess_board, 0, 0),
            expected_moves
        )
