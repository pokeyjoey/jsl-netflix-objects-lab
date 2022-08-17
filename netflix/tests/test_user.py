from src.user import User
from src.viewing import Viewing
from src.user import User
from src.episode import Episode
from src.index import build_store

def test_user_has_name():
    store = build_store()
    user = User(store, name = 'Bob Smith')
    user.name == 'Bob Smith'

def test_user_is_added_to_store():
    store = build_store()
    user = User(store, name = 'Bob Smith')
    assert store['users'][1] == user

def test_user_has_an_id():
    store = build_store()
    user = User(store, name = 'Bob Smith')
    user.id == 1

def test_user_viewings():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    sam = User(store, name = 'Sam Sammi')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    seinfeld_two = Episode(store, title = 'Yada Yada')
    viewing_one = Viewing(store, bob, seinfeld_one)
    viewing_two = Viewing(store, bob, seinfeld_two)
    viewing_three = Viewing(store, sam, seinfeld_two)
    assert bob.viewings() == [viewing_one, viewing_two]

def test_user_episodes():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    sam = User(store, name = 'Sam Sammi')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    seinfeld_two = Episode(store, title = 'Yada Yada')
    viewing_one = Viewing(store, bob, seinfeld_one)
    viewing_two = Viewing(store, bob, seinfeld_two)
    viewing_three = Viewing(store, sam, seinfeld_two)
    assert bob.episodes() == [seinfeld_one, seinfeld_two]

def test_user_find_viewings_for_episode():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    sam = User(store, name = 'Sam Sammi')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    seinfeld_two = Episode(store, title = 'Yada Yada')
    viewing_one = Viewing(store, bob, seinfeld_one)
    viewing_two = Viewing(store, bob, seinfeld_two)
    viewing_three = Viewing(store, sam, seinfeld_two)
    assert bob.find_viewings_for(seinfeld_one) == [viewing_one]

def test_user_last_stop_time_for():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    viewing_one = Viewing(store, bob, seinfeld_one)
    viewing_one.start_time = 0
    viewing_one.stop_time = 40
    viewing_two = Viewing(store, bob, seinfeld_one)
    viewing_two.start_time = 40
    viewing_two.stop_time = 80
    assert bob.last_stop_time_for(seinfeld_one) == 80
