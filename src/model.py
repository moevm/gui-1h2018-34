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
    __movies_json_path = "../movies.json"

    def __init__(self):
        with open(self.__movies_json_path, "r") as f:
            movies = json.load(f)

        self.movies = []
        for m in movies:
            self.movies.append(MovieData(m["title"], m["screenshots_links"], int(m["votes_count"]), m["id"]))
            # todo change votes_count type in json document str -> int



