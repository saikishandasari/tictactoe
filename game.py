import random

class tictactoe:
    def __init__(self, length, player_token):
        self.length = length
        self.board = [['-' for _ in range(length)] for _ in range(length)]
        self.player_token = player_token
        self.bot_token = 'O' if player_token == 'X' else 'X'
        self.spots_left = length ** 2
        self.game_over = False
        print(self)

    def __str__(self):
        str = ''
        for i in range(self.length):
            str += '\n' + '+---'*self.length + '+\n'
            str += '| ' + ' | '.join(self.board[i][:]) + ' |'
        return str + '\n' + '+---'*self.length + '+\n'
    
    def add_token(self, x, y, token):
        """
        Places a given token at (x,y) on the board
        """
        if x >= self.length or y >= self.length or self.board[x][y] != '-':
            print_message('Invalid spot! Please try again.')
            return False
        else:
            self.board[x][y] = token
            self.spots_left -= 1
            print(self)
            print('{} played {},{}\n'.format(token,x,y))
            return True

    def add_bot_token(self):
        """
        Determines the correct spot and places the computer's token.
        TODO: Create an algorithm to place the token strategically. At the moment, places the token in a random spot.
        """
        # check the rows
        for i in range(self.length):
            # check for win
            if self.board[i].count(self.bot_token) == self.length - 1 and self.board[i].count('-') >= 1:
                return self.add_token(i, self.board[i].index('-'), self.bot_token)
            # block the win for player
            if self.board[i].count(self.player_token) == self.length - 1 and self.board[i].count('-') >= 1:
                return self.add_token(i, self.board[i].index('-'), self.bot_token)
        
        # check the columns
        for i in range(self.length):
            column = [self.board[x][i] for x in range(self.length)]
            # check for win
            if column.count(self.bot_token) == len(column) - 1 and column.count('-') >= 1:
                return self.add_token(column.index('-'),i, self.bot_token)
            # block the win for player
            if column.count(self.player_token) == len(column) - 1 and column.count('-') >= 1:
                return self.add_token(column.index('-'),i, self.bot_token)
        
        # check the diagonals
        ltr_diagonal = [self.board[x][x] for x in range(self.length)]
        rtl_diagnoal = [self.board[x][self.length - 1 - x] for x in range(self.length)]
        # check for win
        if ltr_diagonal.count(self.bot_token) == len(ltr_diagonal) - 1 and ltr_diagonal.count('-') >= 1:
            idx = ltr_diagonal.index('-')
            return self.add_token(idx, idx, self.bot_token)

        if rtl_diagnoal.count(self.bot_token) == len(rtl_diagnoal) - 1 and rtl_diagnoal.count('-') >= 1:
            idx = rtl_diagnoal.index('-')
            return self.add_token(idx, self.length - 1 - idx,self.bot_token)           

        # block the win for player
        if ltr_diagonal.count(self.player_token) == len(ltr_diagonal) - 1 and ltr_diagonal.count('-') >= 1:
            idx = ltr_diagonal.index('-')
            return self.add_token(idx, idx, self.bot_token)

        if rtl_diagnoal.count(self.player_token) == len(rtl_diagnoal) - 1 and rtl_diagnoal.count('-') >= 1:
            idx = rtl_diagnoal.index('-')
            return self.add_token(idx, self.length - 1 - idx,self.bot_token)

        # add token in a random spot
        spot_found = False
        while not spot_found:
            x = random.randint(0, self.length - 1)
            y = random.randint(0, self.length - 1)
            if self.board[x][y] == '-':
                spot_found = True
                self.add_token(x, y, self.bot_token)

    def is_winner(self, token):
        for i in range(self.length):
            if self.board[i].count(token) == self.length:
                return True
        
        for i in range(self.length):
            column = [self.board[x][i] for x in range(self.length)]
            if column.count(token) == len(column):
                return True

        ltr_diagonal = [self.board[x][x] for x in range(self.length)]
        rtl_diagnoal = [self.board[x][self.length - 1 - x] for x in range(self.length)]

        if ltr_diagonal.count(token) == len(ltr_diagonal):
            return True

        if rtl_diagnoal.count(token) == len(rtl_diagnoal):
            return True
        
        return False

def print_message(message):
    print('+' + '-' * (len(message)+8) + '+')
    print("|    " + message + "    |")
    print('+' + '-' * (len(message)+8) + '+')

def play():
    print_message("WELCOME TO TIC-TAC-TOE!!!")
    while True:
        board_size = int(input("Enter the size of the board: "))
        if board_size < 3:
            print_message("Invalid value! Please try again!")
        else:
            break
    while True:
        player_token = input("'X' or 'O': ")
        if player_token not in ['X','O']:
            print_message("Invalid value! Please try again!")
        else:
            break

    game = tictactoe(board_size, player_token)

    while not game.game_over:
        # Player turn
        while True:
            x,y = input("Enter position: ").split(',')
            played = game.add_token(int(x), int(y),player_token)
            if played:
                break
        # Check if player won
        if game.is_winner(player_token):
            print_message("GAME OVER! YOU WON THE GAME!")
            game.game_over = True
        # Check if the board is full
        elif game.spots_left == 0:
            print_message("GAME OVER! IT'S A TIE!")
            game.game_over = True
        # Computer's turn
        else:
            game.add_bot_token()
            # Check if computer won
            if game.is_winner(game.bot_token):
                print_message("GAME OVER! COMPUTER WON THE GAME!")
                game.game_over = True
play()