import unittest
from naval_battle import Player
import itertools


def generate_board():
    brd = list()
    for _ in range(12):
        lst = ['~' for _ in range(12)]
        brd.append(lst)
    return brd


def reference_board(icon):
    brd = generate_board()
    for i in range(2, 10):
        brd[i][i if icon == 'о' else 2] = icon
    return brd


class TestStaticMethods(unittest.TestCase):
    def setUp(self):
        self.board = generate_board()

    def test_generate_ships(self):
        self.assertIsInstance(Player.generate_ships(self.board), list)
        self.assertRaises(IndexError, Player.generate_ships, [['~', '~', '~']])
        ships = Player.generate_ships(self.board)
        cells = list(itertools.chain.from_iterable(ships))
        self.assertIn('о', cells)

    def test_generate_board(self):
        self.assertEqual(Player.generate_board(), self.board)
        self.assertEqual(len(Player.generate_board()), 12)
        self.assertIsInstance(Player.generate_board(), list)

    def test_prepare_board(self):
        self.assertIsNotNone(Player.prepare_brd(self.board))
        self.assertIsInstance(Player.prepare_brd(self.board), str)
        rows = Player.prepare_brd(self.board).split('\n')
        self.assertEqual(len(rows), 10)
        self.assertRaises(TypeError, Player.prepare_brd, 2)


class TestInstanceMethods(unittest.TestCase):
    def setUp(self):
        self.player = Player('First')
        self.player.attempts = reference_board('*')
        Player.first_player_board = reference_board('о')

    def test_print_boards(self):
        self.assertIsNone(self.player.print_brds(reference_board('о'), reference_board('*')))
        self.assertRaises(IndexError, self.player.print_brds, 'test', 'test')
        Player.first_player_board = reference_board('о')

    def test_strike(self):
        answer, text, _ = self.player.strike(Player.first_player_board, 5, 5)
        self.assertTrue(answer)
        self.assertEqual(text, 'You hit him !')
        self.assertEqual(self.player.attempts[5][5], 'x')
        answer, text, _ = self.player.strike(Player.first_player_board, 1, 1)
        self.assertTrue(answer)
        self.assertEqual(text, 'You missed :(')
        self.assertEqual(self.player.attempts[1][1], '*')
        answer, text, _ = self.player.strike(Player.first_player_board, 5, 5)
        self.assertFalse(answer)
        self.assertEqual(text, 'smth went wrong')
        answer, text, _ = self.player.strike(Player.first_player_board, 2, 2)
        self.assertFalse(answer)
        self.assertEqual(text, 'You have already pointed there')

    def test_move(self):
        answer = self.player.move(reference_board('о'), reference_board('о'), '22, 22')
        self.assertFalse(answer)
        answer = self.player.move(reference_board('о'), reference_board('о'), '5, 5')
        self.assertTrue(answer)
        answer = self.player.move(reference_board('о'), reference_board('о'), 'dfdfss')
        self.assertFalse(answer)


if __name__ == '__main__':
    unittest.main()