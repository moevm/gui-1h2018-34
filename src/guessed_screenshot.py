from PyQt5.QtCore import QObject, pyqtSlot
from movies import Movies
from random import randrange
import urllib.request

class GuessedScreenshot(QObject):
    __SCREENSHOT_LOCATION__ = "../img/screenshot.jpg"

    def __init__(self):
        super().__init__()

        self.movies = Movies()

        self.new_screenshot()

    def __download_image(self, url, location):
        urllib.request.urlretrieve(url, location)

    def new_screenshot(self, difficult=1):
        movie = self.movies.get_random()
        screenshots = movie["screenshots_urls"]
        screenshots_idx = randrange(len(screenshots))
        screenshot_url = screenshots[screenshots_idx]
        self.__download_image(screenshot_url, self.__SCREENSHOT_LOCATION__)

        self.screenshot = self.__SCREENSHOT_LOCATION__
        self.name = movie["name"]

    def get_screenshot(self):
        return self.screenshot

    def get_name(self):
        return self.name





