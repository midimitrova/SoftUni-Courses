from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def test_is_initialized_mammal(self):
        mammal = Mammal('Test', 'dog', 'woof')

        self.assertEqual('Test', mammal.name)
        self.assertEqual('dog', mammal.type)
        self.assertEqual('woof', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound_correct(self):
        mammal = Mammal('Test', 'dog', 'woof')

        result = "Test makes woof"
        actual = mammal.make_sound()
        self.assertEqual(actual, result)

    def test_get_kingdom(self):
        mammal = Mammal('Test', 'dog', 'woof')

        result = mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        mammal = Mammal('Test', 'dog', 'woof')

        result = "Test is of type dog"
        actual = mammal.info()
        self.assertEqual(actual, result)


if __name__ == '__main__':
    main()
