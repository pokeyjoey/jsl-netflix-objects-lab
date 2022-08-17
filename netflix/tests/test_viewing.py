from src.viewing import Viewing
from src.user import User
from src.episode import Episode
from src.index import build_store

def build_viewing():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    path = './data/seinfeld/1-01-good-news-bad-news/script.txt'
    with open(path, 'r') as file:
        script = file.read()
    seinfeld_one.script = script
    viewing = Viewing(store, bob, seinfeld_one)
    return viewing

def test_viewing_has_user_and_episode_and_store():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    viewing = Viewing(store, bob, seinfeld_one)
    assert viewing.user == bob
    assert viewing.episode == seinfeld_one

def test_viewing_has_an_id():
    store = build_store()
    bob = User(store, name = 'Bob Smiths')
    seinfeld_one = Episode(store, title = 'Good news bad news')
    viewing = Viewing(store, bob, seinfeld_one)

    assert viewing.id == 1

def test_viewing_words():
    viewing = build_viewing()
    viewing.start_time = 0
    viewing.stop_time = 40
    viewing_words = viewing.words()
    assert viewing_words == ['GOOD', 'NEWS,', 'BAD', 'NEWS', 'Written', 'by', 'Larry', 'David', '&', 'Jerry', 'Seinfeld', '(Comedy', 'club)', 'JERRY', 'You', 'know,', 'why', "we're", 'here?', 'To', 'be', 'out,', 'this', 'is', 'out...and', 'out', 'is', 'one', 'of', 'the', 'single', 'most', 'enjoyable', 'experiences', 'of', 'life.', 'People...did', 'you', 'ever', 'hear', 'people', 'talking', 'about', '"We', 'should', 'go', 'out"?', 'This', 'is', 'what', "they're", 'talking', 'about...this', 'whole', 'thing,', "we're", 'all', 'out', 'now,', 'no', 'one', 'is', 'home.', 'Not', 'one', 'person', 'here', 'is', 'home,', "we're", 'all', 'out!', 'There', 'are', 'people', "tryin'", 'to', 'find', 'us,', 'they', "don't", 'know', 'where', 'we', 'are.', '(imitates', 'one', 'of', 'these', 'people', '"tryin\'', 'to', 'find', 'us";', 'pretends', 'his', 'hand', 'is', 'a', 'phone)']
    
def test_script():
    viewing = build_viewing()
    viewing.start_time = 0
    viewing.stop_time = 40
    assert viewing.script() == 'GOOD NEWS, BAD NEWS Written by Larry David & Jerry Seinfeld (Comedy club) JERRY You know, why we\'re here? To be out, this is out...and out is one of the single most enjoyable experiences of life. People...did you ever hear people talking about "We should go out"? This is what they\'re talking about...this whole thing, we\'re all out now, no one is home. Not one person here is home, we\'re all out! There are people tryin\' to find us, they don\'t know where we are. (imitates one of these people "tryin\' to find us"; pretends his hand is a phone)'
