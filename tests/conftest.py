from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO

#В данной директории создаём фикстуры для DAO имитируя выполнения сессии с базой данных


#Создаем фикстуру с моком для DirectorDAO
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="Aleks")
    director_2 = Director(id=2, name="Nik")
    director_3 = Director(id=3, name="Vasiliy")

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])
    director_dao.create = MagicMock(return_value=director_3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao

#Создаем фикстуру с моком для GenreDAO
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Comedy")
    genre_2 = Genre(id=2, name="Thriller")
    genre_3 = Genre(id=3, name="Dramagenre")

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=genre_3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao

#Создаем фикстуру с моком для MovieDAO
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title="New cinima", description="description about new cinima", year=1999, rating=6.0)
    movie_2 = Movie(id=2, title="Superman", description="description about superman", year=2000, rating=8.0)
    movie_3 = Movie(id=3, title="New create", description="description about create new film", year=2022, rating=7.0)

    movie_dao.get_one = MagicMock(return_value=movie_2)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=movie_3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao