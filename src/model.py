import json
import urllib.request
import random

def compute_difficult(votes_count):
    return 1


class MovieData:
    __SCREENSHOT_LOCATION__ = "../img/screenshot.jpg"

    def __init__(self, title, screenshots_links, votes_count, id):
        self.title = title
        self.screenshots_links = screenshots_links
        self.votes_count = votes_count
        self.id = id

    def __download_image(self, url, location):
        urllib.request.urlretrieve(url, location)

    def get_title(self):
        return self.title

    def get_difficult(self):
        return compute_difficult(self.votes_count)

    def get_random_screenshot(self):
        screenshot_link = random.choice(self.screenshots_links)
        self.__download_image(screenshot_link, self.__SCREENSHOT_LOCATION__)
        return self.__SCREENSHOT_LOCATION__

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
    __MOVIES_JSON_PATH = "../movies.json"

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


class MoviesPicker:
    __OPTIONS_COUNT = 4

    def __init__(self, options_count=__OPTIONS_COUNT):
        self.movies = Movies()
        self.options_count = options_count
        self.answer_options = None
        self.picked_movies_history = []

    def pick_movie(self, difficult):
        self.answer_options = self.movies.get_movies(count=1,
                                                     difficult=difficult,
                                                     except_movies_with_ids=self.picked_movies_history)
        self.picked_movies_history.append(self.answer_options[0].get_id())
        self.answer_options += self.movies.get_movies(count=self.options_count - 1,
                                                      difficult=difficult,
                                                      except_movies_with_ids=[self.picked_movies_history[-1]])

    def get_picked_movie(self):
        return self.get_answer_options()[0]

    # return picked movie and (self.options_count - 1) other movies
    def get_answer_options(self):
        if self.answer_options is None:
            raise Exception('Movie is not picked yet')
        return self.answer_options

    def clear_picked_movies_history(self):
        self.picked_movies_history = []


