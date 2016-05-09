def place_piece_on_board(board, piece, x, y):
    moves = piece.get_valid_moves(board, x, y)
    if not moves:
        return False
    board.valid_squares.difference_update({(x, y)})
    board.threatened_squares.update(moves)
    # we need to set the board coordinates in this order
    # as rows come first.
    board.squares[y][x] = str(piece)
    board.num_pieces += 1
    return True


def square_on_board(board_size, x, y):
    """Check if (x,y) is in the boundaries of the board of defined size"""
    len_x, len_y = board_size
    return all((x >= 0, y >= 0, x < len_x, y < len_y))
