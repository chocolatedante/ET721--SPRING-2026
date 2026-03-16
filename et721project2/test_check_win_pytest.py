from main import Connect4


def test_check_win_horizontal():
    game = Connect4()
    for col in range(4):
        game.board[5][col] = 'X'
    assert game.check_win('X') is True


def test_check_win_vertical():
    game = Connect4()
    for row in range(2, 6):
        game.board[row][0] = 'X'
    assert game.check_win('X') is True


def test_check_win_diagonal_down_right():
    game = Connect4()
    game.board[0][0] = 'X'
    game.board[1][1] = 'X'
    game.board[2][2] = 'X'
    game.board[3][3] = 'X'
    assert game.check_win('X') is True


def test_check_win_diagonal_up_right():
    game = Connect4()
    game.board[5][0] = 'X'
    game.board[4][1] = 'X'
    game.board[3][2] = 'X'
    game.board[2][3] = 'X'
    assert game.check_win('X') is True


def test_check_win_no_win():
    game = Connect4()
    game.board[5][0] = 'X'
    game.board[5][1] = 'X'
    game.board[5][2] = 'X'
    game.board[5][3] = 'O'
    assert game.check_win('X') is False


#documentation in main python file