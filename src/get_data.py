from json import loads
from requests_html import HTMLSession

from game import Game
from get_url import get_current_mirror


def get_data():
    session = HTMLSession()
    url = f"{get_current_mirror()}/LiveFeed/Get1x2_Zip?sports=103&count=1000&mode=4&cyberFlag=1&country=1"
    json_data = loads(session.get(url).text)
    info = json_data.get('Value')

    games = []
    for g in info:
        games.append(Game(g.get('I')))

    return games
