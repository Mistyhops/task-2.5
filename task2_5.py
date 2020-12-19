import random

class Ship:
    def __init__(self, number):
        self.number = number

class Board(Ship):
    def __init__(self):
        self.board_pl = ('0 ' * 37).split()
        self.board_AI = ('0 ' * 37).split()

    def print_board_pl(self):
        print('Ваше поле: ')
        print(' ', '| 1 | 2 | 3 | 4 | 5 | 6 |')
        for i in range(6):
            print(i + 1, '|', self.board_pl[0 + i * 6], '|', self.board_pl[1 + i * 6], '|', self.board_pl[2 + i * 6], '|', self.board_pl[3 + i * 6],
                  '|', self.board_pl[4 + i * 6], '|', self.board_pl[5 + i * 6], '|')
        return ''

    def print_board_AI(self):
        print('Поле компьютера: ')
        print(' ', '| 1 | 2 | 3 | 4 | 5 | 6 |')
        for i in range(6):
            print(i + 1, '|', self.board_AI[0 + i * 6], '|', self.board_AI[1 + i * 6], '|', self.board_AI[2 + i * 6],
                  '|', self.board_AI[3 + i * 6],
                  '|', self.board_AI[4 + i * 6], '|', self.board_AI[5 + i * 6], '|')
        return ''

    def win_cond(self):
        if self.board_pl.count('X') == 11:
            return 'Победил компьютер.'
        if self.board_AI.count('X') == 11:
            return 'Вы победили.'
        else:
            return False

class Turn(Board, Ship):
    def turn_player(self):
        try:
            turn_pl = list(map(int, input('Введите сначала номер строки, затем номер столбца через пробел: ').split()))
            if len(turn_pl) == 2 and 1 <= turn_pl[0] <= 6 and 1 <= turn_pl[1] <= 6:
                if self.board_AI[(turn_pl[1] - 1) + (turn_pl[0] - 1) * 6] == '0':
                    if (turn_pl[1] - 1) + (turn_pl[0] - 1) * 6 in ships_ai.number:
                        self.board_AI.pop((turn_pl[1] - 1) + (turn_pl[0] - 1) * 6)
                        self.board_AI.insert((turn_pl[1] - 1) + (turn_pl[0] - 1) * 6, 'X')
                    else:
                        self.board_AI.pop((turn_pl[1] - 1) + (turn_pl[0] - 1) * 6)
                        self.board_AI.insert((turn_pl[1] - 1) + (turn_pl[0] - 1) * 6, 'T')
                else:
                    print('Эта клетка уже занята.')
                    board_var.turn_player()
            else:
                print('Введите корректное значение, например: 1 2.')
                board_var.turn_player()
        except ValueError:
            print('Введите корректное значение, например: 1 2.')
            board_var.turn_player()

    def turn_ai(self):
        int_turn_AI = random.randint(0, 36)
        if self.board_pl[int_turn_AI] == '0':
            if int_turn_AI in ships_pl.number:
                self.board_pl.pop(int_turn_AI)
                self.board_pl.insert(int_turn_AI, 'X')
                board_var.print_board_pl()
                board_var.print_board_AI()
            else:
                self.board_pl.pop(int_turn_AI)
                self.board_pl.insert(int_turn_AI, 'T')
                board_var.print_board_pl()
                board_var.print_board_AI()
        else:
            board_var.turn_ai()

ships_ai = [0, 1, 2, 9, 10, 18, 20, 22, 28, 30, 32]
ships_pl = [0, 1, 2, 9, 10, 18, 20, 22, 28, 30, 32]
ships_ai = Ship(ships_ai)
ships_pl = Ship(ships_pl)

board_var = []
board_var = Turn()

print(board_var.print_board_pl())
print(board_var.print_board_AI())


while True:
    if board_var.win_cond() is False:
        board_var.turn_player()
    if board_var.win_cond() is False:
        board_var.turn_ai()
    else:
        print(board_var.win_cond())
        break

