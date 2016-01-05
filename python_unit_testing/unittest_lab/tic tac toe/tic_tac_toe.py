# You are asked to implement a tic-tac-toe game.
# You are expected to prepare a class named TicTacToeBoard, that implements
# the following methods:
#
# reset_board():
# 	prepares you object for a new game. The return value is not important.
# player_move(x, y, player_number):
# 	accepts a new move from player, at coordinates x, y.
#   returns a BaseException if the player numver is not 1 or 2
#
# When player_move() is called, it should return an integer value with the
# following meaning:
#
#  0 →  No winner, game continues
#  1 →  This is a winning move, the game is over
# -1 →  No winner, no more moves, the game is a draw.


class TicTacToeBoard:
    cols = []
    rows = []
    diag = []
    board = []
    moves = 0

    def __init__(self):
        self.reset_board()

    def update_and_check(self, direction_tracker, player_number):
        if (player_number != 1 and player_number != 2):
            return False
        direction_tracker[player_number-1] += 1
        return True if direction_tracker[player_number-1] == 3 else False

    def player_move(self, x, y, player_number):
        # Sanity Check
        if (player_number == 1 and player_number == 2):
            raise BaseException('Illegal player number.')
        if (self.board[x][y] != 0):
            raise BaseException('This cell is already occupied by player: %d' & board[x][y])
        self.board[x][y] = player_number

        if self.moves > 9:
            return -1

        # Rows
        if self.update_and_check(self.rows[x], player_number): return 1
        # Columns
        if self.update_and_check(self.cols[y], player_number): return 1
        # Diagonal
        if (x==y):
            if self.update_and_check(self.diag[0], player_number): return 1
        # Antidiagonal
        if (x == y-2):
            if self.update_and_check(self.diag[1], player_number): return 1

        self.moves += 1
        return 0

    def reset_board(self):
        self.board = [[0 for y in range(3)] for x in range(3)]
        self.rows = [[0 for y in range(2)] for x in range(3)]
        self.cols = [[0 for y in range(2)] for x in range(3)]
        self.diag = [[0 for y in range(2)] for x in range(2)]
        self.moves = 0
