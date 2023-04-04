from project_test.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie('Titanic', 1997, 9.5)

    def test_is_movie_initialized_correct(self):
        self.assertEqual('Titanic', self.movie.name)
        self.assertEqual(1997, self.movie.year)
        self.assertEqual(9.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_is_validate_wrong(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_name_is_validate_correct(self):
        self.assertEqual('Titanic', self.movie.name)

    def test_year_is_validate_wrong(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1885
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_year_is_validate_correct(self):
        self.assertEqual(1997, self.movie.year)

    def test_add_actors_when_name_is_added_for_first_time(self):
        self.movie.add_actor('Leonardo DiCaprio')
        self.assertEqual(1, len(self.movie.actors))
        self.assertEqual(['Leonardo DiCaprio'], self.movie.actors)

    def test_add_actors_when_actor_is_already_in_list(self):
        self.movie.add_actor('Leonardo DiCaprio')
        self.movie.add_actor('Kate Winslet')
        self.assertEqual(['Leonardo DiCaprio', 'Kate Winslet'], self.movie.actors)

        result = self.movie.add_actor('Leonardo DiCaprio')
        self.assertEqual("Leonardo DiCaprio is already added in the list of actors!", result)

    def test_gt_method_when_first_movie_is_better(self):
        first_movie = Movie('Titanic', 1997, 9.5)
        second_movie = Movie('Inception', 2010, 8.8)

        result = str(first_movie > second_movie)

        self.assertEqual('"Titanic" is better than "Inception"', result)

    def test_gt_method_when_second_movie_is_better(self):
        first_movie = Movie('Titanic', 1997, 8.5)
        second_movie = Movie('Inception', 2010, 8.8)

        result = str(first_movie > second_movie)

        self.assertEqual('"Inception" is better than "Titanic"', result)

    def test_repr_method(self):
        self.movie.add_actor('Leonardo DiCaprio')
        self.movie.add_actor('Kate Winslet')

        result = "Name: Titanic\nYear of Release: 1997\nRating: 9.50\nCast: Leonardo DiCaprio, Kate Winslet"

        actual_result = str(self.movie)

        self.assertEqual(result, actual_result)


if __name__ == '__main__':
    main()
