from src.viewing import Viewing

class NetflixPlayer:

    def play_viewing(self, viewing):
        print(viewing.script())

    def play_episode_for(self, store, user, episode):
        # get episodes viewed by the user
        previously_viewed_episodes = user.find_viewings_for(episode)
        start_time = 0

        # if the user was watching this episode previously
        # - start this viewing where the last viewing ended
        if previously_viewed_episodes:
            start_time = user.last_stop_time_for(episode)

        viewing = Viewing(store, user, episode)
        viewing.start_time = start_time
        viewing.end_time = episode.end_time()


