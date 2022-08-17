class Episode:

    def __init__(self, store, title):
        self._title = title
        self._id = len(store['episodes']) + 1
        self._script = None
        self.store = store
        store['episodes'][self._id] = self

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, script):
        self._script = script

    def words(self):
        return self._script.split()

    def viewings(self):
        return [viewing for viewing in self.store['viewings'].values() if self.id == viewing.episode.id]

    def users(self):
        return [viewing.user for viewing in self.store['viewings'].values() if self.id ==
                viewing.episode.id]

    def end_time(self):
        return len(self.words()) * 2.5

