from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Test', 10, 100, 50)
        self.enemy = Hero('Test2', 10, 100, 50)

    def test_is_initialized_hero_correct(self):
        hero = Hero('Test', 10, 100, 50)

        self.assertEqual('Test', hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(50, hero.damage)

    def test_battle_with_himself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_negative_ex_raises(self):
        self.hero.health = -50
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_hero_health_zero_ex_raises(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_negative_ex_raises(self):
        self.enemy.health = -50
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_enemy_health_zero_ex_raises(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_returns_draw_when_both_heroes_die(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual('Draw', result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_hero_levels_up_after_win(self):
        enemy = Hero('Test2', 1, 100, 50)

        result = self.hero.battle(enemy)

        self.assertEqual('You win', result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(-400, enemy.health)

    def test_battle_enemy_hero_levels_up_if_survive(self):
        hero = Hero('Test', 1, 100, 50)
        enemy = Hero('Test2', 1, 100, 50)

        result = hero.battle(enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(55, enemy.damage)
        self.assertEqual(50, hero.health)

    def test_str_method(self):
        result = f"Hero Test: 10 lvl\n" \
                 f"Health: 100\n" \
                 f"Damage: 50\n"

        actual = str(self.hero)

        self.assertEqual(result, actual)


if __name__ == '__main__':
    main()
