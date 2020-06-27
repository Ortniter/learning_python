from random import randrange
from os import system, name
from time import sleep


class Player:
    first_player_board = None
    second_player_board = None

    def __init__(self, number):
        self.attempts = None
        self.points = 0
        self.number = number

    def strike(self, rival_brd, row, column):
        icon = rival_brd[row][column]
        if self.attempts[row][column] != '*':
            if icon == 'о':
                rival_brd[row][column] = 'x'
                self.attempts[row][column] = 'x'
                return True, 'You hit him !', 1
            elif icon == '~':
                self.attempts[row][column] = '*'
                return True, 'You missed :(', 0
            else:
                return False, 'smth went wrong', 0
        else:
            return False, 'You have already pointed there', 0

    @staticmethod
    def generate_ships(brd):
        check = 0
        while check != 8:
            row, column = randrange(1, 11), randrange(1, 11)
            check_lst = brd[row - 1][column - 1:column + 2] + brd[row][column - 1:column + 2] + brd[row + 1][
                column - 1:column + 2]
            if all([True if i == '~' else False for i in check_lst]):
                brd[row][column] = 'о'
                check += 1
            else:
                continue
        return brd

    @staticmethod
    def generate_board():
        brd = list()
        for _ in range(12):
            lst = ['~' for _ in range(12)]
            brd.append(lst)
        return brd

    @staticmethod
    def prepare_brd(row_brd):
        count = 0
        nice_brd = ''
        for row in row_brd[1:11]:
            count += 1
            string = ' '.join(row[1:11])
            if count == 10:
                nice_brd += f'{count}| {string}'
            else:
                nice_brd += f'{count} | {string}\n'
        return nice_brd

    def print_brds(self, player_brd, player_attempts):
        brd_split = self.prepare_brd(player_brd).split('\n')
        attempts_split = self.prepare_brd(player_attempts).split('\n')
        string = f'{self.number} player | Your points {self.points}\n{26 * "__"}\n'
        string += f'Your Board{18 * " "}Your attempts\n'
        string += '0 | 1 2 3 4 5 6 7 8 9 10    0 | 1 2 3 4 5 6 7 8 9 10\n'
        for i in range(10):
            string += f'{brd_split[i]}     {attempts_split[i]}\n'
        print(string)

    def move(self, players_board, rival_board, move):
        coordinates = move.split(',')
        try:
            coordinates_check = all(
                [True if int(n) in range(1, 11) else False for n in coordinates])
            if coordinates_check:
                coordinates_check = len(coordinates) == 2
        except ValueError:
            print('Coordinates have to be only numbers')
            sleep(3)
            clear()
            return False
        if coordinates_check:
            clear()
            strike_check, text, point = self.strike(
                rival_board, int(coordinates[0]), int(coordinates[1]))
            self.points += point
            if strike_check:
                if self.points == 8:
                    print(f'{self.number} Player has won !')
                    sleep(3)
                    return 'End'
                else:
                    self.print_brds(players_board, self.attempts)
                    print(text)
                    return True
            else:
                print(text)
                sleep(3)
                clear()
                return False
        else:
            print(
                'Please check that you entered two coordinates and every coordinate in range from 1 to 10')
            sleep(3)
            clear()
            return False


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':
    player_one = Player('First')
    Player.first_player_board = Player.generate_ships(Player.generate_board())
    player_one.attempts = Player.generate_board()

    player_two = Player('Second')
    Player.second_player_board = Player.generate_ships(Player.generate_board())
    player_two.attempts = Player.generate_board()

    count = 1
    clear()
    while True:
        if count % 2:
            player_one.print_brds(
                Player.first_player_board, player_one.attempts)
            print()
            action = input('Choose coordinates: ')
            response = player_one.move(
                Player.first_player_board, Player.second_player_board, action)
            if response == 'End':
                break
            elif response:
                input('Press enter to clear: ')
                clear()
                input('Press enter to switch to Second Player: ')
                clear()
                count += 1
            else:
                continue
        else:
            player_two.print_brds(
                Player.second_player_board, player_two.attempts)
            print()
            action = input('Choose coordinates: ')
            response = player_two.move(
                Player.second_player_board, Player.first_player_board, action)
            if response == 'End':
                break
            elif response:
                input('Press enter to clear: ')
                clear()
                input('Press enter to switch to Second Player: ')
                clear()
                count += 1
            else:
                continue

    print('The End')
