WORDS_VIEWED_PER_SECOND = 2.5

class Viewing:

    def __init__(self, store, user, episode):
        self._user = user
        self._episode = episode
        self._start_time = 0
        self._stop_time = 0
        self._id = len(store['viewings']) + 1
        store['viewings'][self._id] = self

    @property
    def episode(self):
        return self._episode

    @episode.setter
    def episode(self, episode):
        self._episode = episode

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def stop_time(self):
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        self._stop_time = stop_time

    def words(self):
        number_of_words_read_in_viewing = \
            int((self._stop_time - self._start_time) * WORDS_VIEWED_PER_SECOND)
        all_words = self._episode.words()
        words_in_viewing = all_words[:number_of_words_read_in_viewing]
        return words_in_viewing

    def script(self):
        return ' '.join(self.words())
