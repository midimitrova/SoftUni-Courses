from project_test.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self):
        self.team = Team('Levski')

    def test_is_team_initialized_correct(self):
        self.assertEqual('Levski', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_with_invalid_data(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = '4Sk.'
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_name_with_valid_data(self):
        self.assertEqual('Levski', self.team.name)

    def test_add_member_when_member_added_for_first_time(self):
        result = self.team.add_member(Tisho=25)

        self.assertEqual(1, len(self.team.members))
        self.assertEqual("Successfully added: Tisho", result)
        self.assertEqual({'Tisho': 25}, self.team.members)

    def test_add_member_when_member_added_for_second_time(self):
        result = self.team.add_member(Tisho=25)

        self.assertEqual(1, len(self.team.members))
        self.assertEqual("Successfully added: Tisho", result)
        self.assertEqual({'Tisho': 25}, self.team.members)

        result = self.team.add_member(Tisho=25, Ceco=24, Misho=23)
        self.assertEqual(3, len(self.team.members))
        self.assertEqual("Successfully added: Ceco, Misho", result)
        self.assertEqual({'Tisho': 25, 'Ceco': 24, 'Misho': 23}, self.team.members)

    def test_remove_player_if_name_exist(self):
        self.team.add_member(Tisho=25, Ceco=24)

        result = self.team.remove_member('Tisho')

        self.assertEqual("Member Tisho removed", result)
        self.assertEqual(1, len(self.team.members))
        self.assertEqual({'Ceco': 24}, self.team.members)

    def test_remove_player_if_name_do_not_exist(self):
        result = self.team.remove_member('Tisho')

        self.assertEqual("Member with name Tisho does not exist", result)
        self.assertEqual(0, len(self.team.members))
        self.assertEqual({}, self.team.members)

    def test_gt_method_when_first_team_is_larger(self):
        first_team = Team('Levski')
        second_team = Team('CSKA')

        first_team.add_member(Tisho=25, Ceco=24, Misho=23)
        second_team.add_member(Niki=22, Ivan=20)

        result = first_team > second_team

        self.assertFalse(first_team < second_team)
        self.assertTrue(first_team > second_team)
        self.assertEqual(True, result)

    def test_gt_method_when_second_team_is_larger(self):
        first_team = Team('Levski')
        second_team = Team('CSKA')

        first_team.add_member(Tisho=25, Ceco=24)
        second_team.add_member(Niki=22, Ivan=20, Misho=23)

        result = second_team > first_team

        self.assertFalse(first_team > second_team)
        self.assertTrue(first_team < second_team)
        self.assertEqual(True, result)

    def test_len_method(self):
        self.team.add_member(Tisho=25, Ceco=24, Misho=23)

        self.assertEqual(3, len(self.team.members))

    def test_add_method(self):
        first_team = Team('Levski')
        second_team = Team('CSKA')

        first_team.add_member(Tisho=25, Ceco=24)
        second_team.add_member(Misho=23)

        merged = first_team + second_team

        self.assertEqual('LevskiCSKA', merged.name)
        self.assertEqual(3, len(merged))
        self.assertEqual({'Tisho': 25, 'Ceco': 24, 'Misho': 23}, merged.members)

    def test_str_method(self):
        self.team.add_member(Ceco=24, Misho=23)

        result = "Team name: Levski\nMember: Ceco - 24-years old\nMember: Misho - 23-years old"

        self.assertEqual(result, str(self.team))


if __name__ == '__main__':
    main()
