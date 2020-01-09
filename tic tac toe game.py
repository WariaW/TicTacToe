import os


class TicTacToe():
    def __init__(self, size):
        self.size = int(size)
        self.board = [[' ']*self.size for i in range(self.size)]
        self.print_game_board()
        self.diag1 = lambda: [self.board[i][i] for i in range(self.size)]
        self.diag2 = lambda: [self.board[i][self.size - 1 - i] for i in range(self.size)]

    def print_game_board(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(' ---', end = '')
            print("")
            for j in range(0, self.size):
                print("| {} ".format(self.board[i][j]), end = '')
            print("|")
        for i in range(0, self.size):
            print(' ---', end = '')
        print("")



    def find_winner(self):
        for i in range(0, self.size):
            if (self.board[i].count(self.board[i][0]) == self.size):
                return self.board[i][0]
            elif ([row[i] for row in self.board].count(self.board[0][i]) == self.size):
                return self.board[0][i]

        if (self.diag1().count(self.diag1()[0]) == self.size):
            return self.board[0][0]
        if (self.diag2().count(self.diag2()[0]) == self.size):
            return self.board[0][self.size]

        return 0

    def player_turn(self, player):
        coordinates = input("Player {} turn. Enter coordinates in form: rowNo,colNo ".format(player + 1)).split(',')
        row, col = coordinates[0], coordinates[1]
        if (not (row.isdigit() and col.isdigit()) or coordinates.__len__() > 2):
            print("Wrong form! Try again! Example: user want to set x or o in 3rd row and 2nd column. Correct input is: 3,2")
            while (not (row.isdigit() and col.isdigit()) or coordinates.__len__() > 2):
                coordinates = input("Player {} turn. Enter coordinates in form: rowNo,colNo ".format(player + 1)).split(
                    ',')
                row, col = coordinates[0], coordinates[1]
        if (self.board[int(row) - 1][int(col) - 1] != ' '):
            print("This spot is occupied! Try again with another coordinates!")
            while (self.board[int(row) - 1][int(col) - 1] != ' '):
                coordinates = input("Player {} turn. Enter coordinates in form: rowNo,colNo ".format(player + 1)).split(',')
                row, col = coordinates[0], coordinates[1]
                if (not (row.isdigit() and col.isdigit()) or coordinates.__len__() > 2):
                    print("Wrong form! Try again! Example: user want to set x or o in 3rd row and 2nd column. Correct input is: 3,2")
                    while (not (row.isdigit() and col.isdigit()) or coordinates.__len__() > 2):
                        coordinates = input("Player {} turn. Enter coordinates in form: rowNo,colNo ".format(player + 1)).split(',')
                        row, col = coordinates[0], coordinates[1]
        return row, col


    def game(self):
        player = 0
        tictac = ['x', 'o']
        for i in range(0, self.size*2 - 1):
            row, col = self.player_turn(player)
            self.board[int(row) - 1][int(col) - 1] = tictac[player]
            player = not player
            self.print_game_board()
        result = self.find_winner()
        while(result == 0):
            row, col = self.player_turn(player)
            self.board[int(row) - 1][int(col) - 1] = tictac[player]
            player = not player
            self.print_game_board()
            result = self.find_winner()
        print('Player {} won the game! \n'.format(tictac.index(result) + 1))

def menu():
    print("TIC TAC TOE!")
    return input("Enter G to play or any other key to escape ")

if __name__ == "__main__":
    while(menu() == 'G'):
        size = input("Set size of game board: ")
        TicTacToeGame = TicTacToe(size)
        # winner_is_2 = [[2, 1, 2],
        #                [0, 1, 0],
        #                [1, 1, 1]]
        # TicTacToeGame.board = winner_is_2
        # print("The winner is: {}".format((TicTacToeGame.find_winner())))
        TicTacToeGame.game()
