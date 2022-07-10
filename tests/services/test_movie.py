import pytest

from service.movie import MovieService

#Создаю класс для тестирования MovieService
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(2)
        assert movie is not None
        assert movie.title == "Superman"
        assert movie.description == "description about superman"
        assert movie.year == 2000
        assert movie.rating == 8.0

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0
        assert len(movies) == 2

    def test_create(self):
        movie_d = {'title': 'New create'}
        new_movie = self.movie_service.create(movie_d)
        assert new_movie.id is not None

    def test_update(self):
        movie = self.movie_service.update(1)

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None