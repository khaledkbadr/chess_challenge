import unittest
import copy
from models.chessboard import ChessBoard


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard(3, 3)

    def test_ChessBoard_instance_has_expected_default_values_and_fields(self):
        self.assertEqual(self.chess_board.len_x, 3)
        self.assertEqual(self.chess_board.len_x, 3)
        expected_squares = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(self.chess_board.squares, expected_squares)
        self.assertEqual(self.chess_board.threatened_squares, set())
        expected_valid_squares = {(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)}
        self.assertEqual(self.chess_board.valid_squares, expected_valid_squares)
        self.assertEqual(len(self.chess_board.valid_squares), 9)
        self.assertEqual(self.chess_board.num_pieces, 0)

    def test_ChessBoard_instance_copy_has_expected_default_values_and_fields(self):
        _chess_board = copy.copy(self.chess_board)
        self.assertEqual(_chess_board.len_x, 3)
        self.assertEqual(_chess_board.len_x, 3)
        expected_squares = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(_chess_board.squares, expected_squares)
        self.assertEqual(_chess_board.threatened_squares, set())
        expected_valid_squares = {(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)}
        self.assertEqual(_chess_board.valid_squares, expected_valid_squares)
        self.assertEqual(len(_chess_board.valid_squares), 9)
        self.assertEqual(_chess_board.num_pieces, 0)

    def test_ChessBoard_instance_string_representation(self):
        self.assertEqual(str(self.chess_board), 9 * '.')
