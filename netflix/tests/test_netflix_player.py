from src.services.netflix_player import NetflixPlayer
from src.viewing import Viewing
from src.episode import Episode
from src.user import User
from src.index import build_store

def build_viewing(store):
    
    bob = User(store, name = 'Bob Smiths')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    path = './data/seinfeld/1-01-good-news-bad-news/script.txt'
    with open(path, 'r') as file:
        script = file.read()
    seinfeld_one.script = script
    viewing = Viewing(store, bob, seinfeld_one)
    viewing.start_time = 0
    viewing.stop_time = 40
    return viewing

def test_play_viewing():
    store = build_store()
    viewing = build_viewing(store)
    player = NetflixPlayer()
    player.play_viewing(viewing)

def test_play_episode_when_partially_viewed():
    store = build_store()
    viewing = build_viewing(store)

    player = NetflixPlayer()
    episode = viewing.episode
    user = viewing.user
    player.play_episode_for(store, user, episode)
    recent_viewing = viewing.user.viewings()[-1]

    assert recent_viewing.start_time == viewing.stop_time
    # creates a new viewing from where left off
