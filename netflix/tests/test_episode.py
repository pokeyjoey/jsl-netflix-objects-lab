from src.episode import Episode
from src.user import User
from src.viewing import Viewing
from src.index import build_store

def test_episode_has_title():
    store = build_store()
    episode = Episode(store, title = 'Good news bad news')
    episode.title == 'Good news bad news'

def test_episode_is_added_to_store():
    store = build_store()
    episode = Episode(store, title = 'Good news bad news')
    assert store['episodes'][1] == episode

def test_episode_has_an_id():
    store = build_store()
    episode = Episode(store, title = 'Good news bad news')
    episode.id == 1

def test_script_words_removes_empty_strings_and_just_new_lines():
    # https://imsdb.com/TV/Seinfeld.html
    # https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    store = build_store()
    path = './data/seinfeld/1-01-good-news-bad-news/script.txt'
    with open(path, 'r') as file:
        script = file.read()
    episode = Episode(store, title = 'Good news bad news')
    episode.script = script
    assert episode.words()[:20] == ['GOOD', 'NEWS,', 'BAD', 'NEWS', 'Written', 'by', 'Larry', 'David', '&', 'Jerry', 'Seinfeld', '(Comedy', 'club)', 'JERRY', 'You', 'know,', 'why', "we're", 'here?', 'To']


def test_episode_viewings():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    sam = User(store, name = 'Sam Sammi')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    seinfeld_two = Episode(store, title = 'Yada Yada')
    viewing_one = Viewing(store, bob, seinfeld_one)
    viewing_two = Viewing(store, bob, seinfeld_two)
    viewing_three = Viewing(store, sam, seinfeld_two)
    viewing_four = Viewing(store, sam, seinfeld_one)
    assert seinfeld_one.viewings() == [viewing_one, viewing_four]

def test_episode_users():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    sam = User(store, name = 'Sam Sammi')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    seinfeld_two = Episode(store, title = 'Yada Yada')
    viewing_one = Viewing(store, bob, seinfeld_one)
    viewing_two = Viewing(store, bob, seinfeld_two)
    viewing_three = Viewing(store, sam, seinfeld_two)
    viewing_four = Viewing(store, sam, seinfeld_one)
    assert seinfeld_one.users() == [bob, sam]

def test_episode_end_time():
    store = build_store()
    path = './data/seinfeld/1-01-good-news-bad-news/script.txt'
    with open(path, 'r') as file:
        script = file.read()
    episode = Episode(store, title = 'Good news bad news')
    episode.script = script
    assert episode.end_time() == len(episode.words()) * 2.5


# # def test_play_script():
# #     store = build_store()
# #     path = './data/seinfeld/1-01-good-news-bad-news/script.txt'
# #     with open(path, 'r') as file:
# #         script = file.read()
# #     episode = Episode(store, title = 'Good news bad news')
# #     episode.script = script
    
