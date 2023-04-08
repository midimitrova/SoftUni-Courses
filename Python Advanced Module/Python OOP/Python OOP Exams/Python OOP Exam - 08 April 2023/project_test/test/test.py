from project_test.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer('Mimi', 28, 100)

    def test_is_player_initialized_correct(self):
        self.assertEqual('Mimi', self.player.name)
        self.assertEqual(28, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_with_invalid_data(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Mi'
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_with_valid_data(self):
        self.assertEqual('Mimi', self.player.name)

    def test_age_with_invalid_data(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_age_with_valid_data(self):
        self.assertEqual(28, self.player.age)

    def test_add_new_win_when_tournament_name_not_in_wins(self):
        self.assertEqual([], self.player.wins)

        self.player.add_new_win('Harmony')

        self.assertEqual(['Harmony'], self.player.wins)
        self.assertEqual(1, len(self.player.wins))

    def test_add_new_win_when_tournament_name_is_already_in_wins(self):
        self.assertEqual([], self.player.wins)

        self.player.add_new_win('Harmony')
        self.player.add_new_win('Babolat')

        self.assertEqual(['Harmony', 'Babolat'], self.player.wins)

        result = self.player.add_new_win('Harmony')

        self.assertEqual("Harmony has been already added to the list of wins!", result)

    def test_lt_method_when_first_is_less(self):
        first = TennisPlayer('Mimi', 28, 50)
        second = TennisPlayer('Ivan', 24, 100)

        result = first < second

        self.assertEqual('Ivan is a top seeded player and he/she is better than Mimi', result)

    def test_lt_method_when_second_is_less(self):
        first = TennisPlayer('Mimi', 28, 100)
        second = TennisPlayer('Ivan', 24, 50)

        result = first < second

        self.assertEqual('Mimi is a better player than Ivan', result)

    def test_str_method(self):
        self.player.add_new_win('Harmony')
        self.player.add_new_win('Babolat')

        result = "Tennis Player: Mimi\n" \
                 "Age: 28\n" \
                 "Points: 100.0\n" \
                 "Tournaments won: Harmony, Babolat"

        self.assertEqual(result, str(self.player))



if __name__ == '__main__':
    main()
