from PyQt5.QtCore import QObject, pyqtSlot
import json
from random import randrange


class Movies:
    __movies_json_path = "../movies.json"

    def __init__(self):
        with open(self.__movies_json_path, "r") as f:
            self.movies_db = json.load(f)

    def __compute_difficult(self, vote_count):
        return 1

    def __parse_move_data(self, movie_data):
        # {"id":"298","voteCount":"98389","name":"\u041b\u044e\u0434\u0438 \u0418\u043a\u0441 2",
        # "cadres":"974092 974091 _mv_24917 _mv_24912 _mv_24911"},

        return dict(difficult=self.__compute_difficult(int(movie_data["voteCount"])),
                    name=movie_data["name"],
                    screenshots_urls=["http://kinopoisk.ru/images/kadr/{}.jpg".format(tail) for tail in movie_data["cadres"].split()])

    def get_random(self):
        i = randrange(len(self.movies_db))
        row_movie_data = self.movies_db[i]
        return self.__parse_move_data(row_movie_data)