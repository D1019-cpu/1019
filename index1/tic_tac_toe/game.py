import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # using a single list to represent 3x3
        self.current_winner = None # keep track of winner

    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves


    def empty_squares(self):
        return ' ' in self.board

    
    def num_empty_squares(self):
        return self.board.count(' ')


    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return True, if invalid return False
        if self.board[square] == ' ':
            self.board[square] = letter

            if self.is_winner(square, letter):
                self.current_winner = letter

            return True
        return False


    def is_winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        
        # check diagonals
        # [0,4,8] or [2,4,6]
        if square % 2 == 0:
            if (self.board[0] == self.board[4] == self.board[8] == letter) or \
                (self.board[2] == self.board[4] == self.board[6] == letter):
                return True
        
        return False


def play(game, x_player, o_player, print_game=True):
    """Return the winner of the game or None for a tie."""

    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter 
    
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            # switch letter using ternary operator
            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(0.5)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player)
