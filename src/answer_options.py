from PyQt5.QtCore import QObject, pyqtSlot
from movies import Movies


class AnswerOptions(QObject):
    def __init__(self):
        super().__init__()

        self.movies = Movies()

    def get_options(self, count, not_in=None, difficult=1):
        # todo rename not_in

        if not_in is None:
            not_in = []

        # todo more efficient algorithm
        result = set()
        while len(result) < count:
            option = self.movies.get_random()["name"]
            if (option not in not_in) and (option not in result):
                result.add(option)

        return result