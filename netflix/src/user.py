class User:

    def __init__(self, store, name):
        self._name = name
        self._id = len(store['users']) + 1
        store['users'][self._id] = self
        self.store = store

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def viewings(self):
        viewings = \
            [viewing for viewing in self.store['viewings'].values() if viewing.user.id == self._id]
        return viewings

    def episodes(self):
        episodes = \
                [episode for episode in self.store['episodes'].values() if self._id in [viewing.episode.id for viewing in self.viewings()]]
        return episodes

    def find_viewings_for(self, episode):
        viewings = \
            [viewing for viewing in self.store['viewings'].values() if episode.id == viewing.episode.id]
        return viewings

    def last_stop_time_for(self, episode):
        viewings = self.find_viewings_for(episode)
        return viewings[-1].stop_time

