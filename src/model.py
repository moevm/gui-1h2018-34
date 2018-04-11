import json
import urllib.request
import random
import os
import collections


def compute_difficult(votes_count):
    return 1


class MovieData:
    __SCREENSHOT_LOCATION = "../img/screenshot{}.jpg"

    def __init__(self, title, screenshots_links, votes_count, id):
        self.title = title
        self.screenshot_link = random.choice(screenshots_links)
        self.votes_count = votes_count
        self.id = id

        self.__screenshot_location = self.__SCREENSHOT_LOCATION.format(id)
        self.__is_screenshot_downloaded = False

    def __del__(self):
        if self.__is_screenshot_downloaded:
            os.remove(self.__screenshot_location)
            self.__is_screenshot_downloaded = False

    def get_title(self):
        return self.title

    def get_difficult(self):
        return compute_difficult(self.votes_count)

    def download_screenshot(self):
        if not self.__is_screenshot_downloaded:
            urllib.request.urlretrieve(self.screenshot_link, self.__screenshot_location)
            self.__is_screenshot_downloaded = True

    def get_screenshot(self):
        self.download_screenshot()
        return self.__screenshot_location

    def get_id(self):
        return self.id


class Movies:
    """
        {'votes_count': '100',
        'title': 'Давай! Давай!',
        'screenshots_links':
            ['http://kinopoisk.ru/images/kadr/633729.jpg',
            'http://kinopoisk.ru/images/kadr/633728.jpg',
            'http://kinopoisk.ru/images/kadr/633727.jpg',
            'http://kinopoisk.ru/images/kadr/633726.jpg',
            'http://kinopoisk.ru/images/kadr/633725.jpg'],
        'id': 718},
    """
    __MOVIES_JSON_PATH = "../data/movies.json"

    def __init__(self):
        with open(self.__MOVIES_JSON_PATH, "r") as f:
            movies = json.load(f)

        self.movies = []
        for m in movies:
            self.movies.append(MovieData(m["title"], m["screenshots_links"], int(m["votes_count"]), m["id"]))
            # todo change votes_count type in json document str -> int

    def get_movies(self, count=1, difficult=None, except_movies_with_ids=None):
        movies = self.movies
        if difficult is not None:
            movies = filter(lambda m: m.get_difficult() == difficult, movies)
        if except_movies_with_ids is not None:
            movies = filter(lambda m: m.get_id() not in except_movies_with_ids, movies)
        return random.sample(list(movies), count)


class PickedMovies:
    def __init__(self, answer, answer_options):
        # answer_options is a list of MovieData objects. It includes answer
        self.answer = answer
        self.answer_options = answer_options

    def get_answer(self):
        return self.answer

    def get_answer_options(self):
        return self.answer_options


class MoviesPicker:
    __OPTIONS_COUNT = 4

    def __init__(self, options_count=__OPTIONS_COUNT):
        self.movies = Movies()
        self.options_count = options_count
        self.picked_movies_history = []
        self.picked_movies_cash = collections.deque([None, None], maxlen=2)

    def __pick_movies(self, difficult):
        answer_options = self.movies.get_movies(count=1,
                                                difficult=difficult,
                                                except_movies_with_ids=self.picked_movies_history)
        self.picked_movies_history.append(answer_options[0].get_id())
        answer_options += self.movies.get_movies(count=self.options_count - 1,
                                                 difficult=difficult,
                                                 except_movies_with_ids=[self.picked_movies_history[-1]])

        return PickedMovies(answer_options[0], answer_options)

    def pick_movies(self, difficult):
        # todo download asynchronously
        result = self.picked_movies_cash[-1]
        if result is None or result.get_answer().get_difficult() != difficult:
            self.picked_movies_cash.append(self.__pick_movies(difficult))
            result = self.picked_movies_cash[-1]

        next_pick = self.__pick_movies(difficult)
        next_pick.answer.download_screenshot()
        self.picked_movies_cash.append(next_pick)

        return result




