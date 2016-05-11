import unittest
from models.chessboard import ChessBoard
from models.chess_pieces.king import King
from models.helpers import (place_piece_on_board,
                            square_on_board, empty_copy, pretty_print_board)


class HelpersTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard(3, 3)
        self.piece = King()

    def test_place_piece_on_board(self):
        self.assertTrue(place_piece_on_board(self.chess_board, self.piece, 0, 0))
        self.assertFalse(place_piece_on_board(self.chess_board, self.piece, 0, 1))

    def test_square_on_board(self):
        self.assertTrue(square_on_board((3, 3), 1, 2))
        self.assertFalse(square_on_board((3, 3), 1, 4))

    def test_empty_copy(self):
        _copy = empty_copy(self.piece)
        self.assertEqual(_copy.__class__.__name__, 'King')

    def test_pretty_print_board(self):
        board_representation = '┌───┐\n│   │\n└───┘\n\n'
        self.assertEqual(pretty_print_board(1, '.'), board_representation)
