from abc import ABCMeta, abstractmethod


class ChessPiece(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def get_moves(cls, board_dimensions, x, y):
        pass
