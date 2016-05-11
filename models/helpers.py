def place_piece_on_board(board, piece, x, y):
    """Return true if piece is placed on board successfully"""
    moves = piece.get_valid_moves(board, x, y)
    if not moves:
        return False
    board.valid_squares.difference_update({(x, y)})
    board.threatened_squares.update(moves)
    # we need to set the board coordinates in this order
    # as rows come first.
    board.squares[y][x] = piece.representation
    board.num_pieces += 1
    return True


def square_on_board(board_size, x, y):
    """Check if (x,y) is in the boundaries of the board of defined size"""
    len_x, len_y = board_size
    return all((x >= 0, y >= 0, x < len_x, y < len_y))


def empty_copy(obj):
    """Return an empty instance of the same class as the object"""
    class Empty(obj.__class__):
        def __init__(self):
            pass

    new_copy = Empty()
    new_copy.__class__ = obj.__class__
    return new_copy


def pretty_print_board(len_x, board_string):
    """Pretty print board representation"""
    def chunks(txt):
        for i in range(0, len(txt), len_x):
            yield txt[i:i + len_x]

    horiz_size_x = [u'───'] * len_x
    upper_box_line = u'┌{}┐\n'.format(u'┬'.join(horiz_size_x))
    lower_box_line = u'└{}┘\n'.format(u'┴'.join(horiz_size_x))
    middle_box_line = u'├{}┤\n'.format(u'┼'.join(horiz_size_x))
    content = middle_box_line.join(
        [u'│' + u'│'.join(
            [' {} '.format(c.replace('.', ' ')) for c in r]) + u'│\n'
         for r in chunks(board_string)])
    return upper_box_line + content + lower_box_line + '\n'
