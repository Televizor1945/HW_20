import pytest

from service.genre import GenreService

#Создаю класс для тестирования GenreService
class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.name == "Comedy"

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0
        assert len(genres) == 2

    def test_create(self):
        genre_d = {'name': 'Melodrama'}
        new_genre = self.genre_service.create(genre_d)
        assert new_genre.id is not None

    def test_update(self):
        genre = self.genre_service.update(1)

    def test_delete(self):
        res = self.genre_service.delete(1)
        assert res is None