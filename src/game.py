from json import loads
from requests_html import HTMLSession

from get_url import get_current_mirror


class Game:
    def __init__(self, id):
        self._id = id
        self._fw_coef = 0
        self.get_info_by_id()
        self.init_fighters()
        self.coefs_on_wins_in_rounds()
        self.is_fw_coef()

    def __repr__(self):
        return f"""{self._left_fighter} - {self._right_fighter}
П1 в раунде: {self._first_win_coef}
П2 в раунде: {self._second_win_coef}
Сумма: {round(self._first_win_coef + self._second_win_coef, 3)}
Чистая победа: {self._fw_coef}"""


    def __str__(self):
        return f"""{self._left_fighter} - {self._right_fighter}
П1 в раунде: {self._first_win_coef}
П2 в раунде: {self._second_win_coef}
Сумма: {round(self._first_win_coef + self._second_win_coef, 3)}
Чистая победа: {self._fw_coef}"""


    def get_info_by_id(self):
        session = HTMLSession()
        url = f"{get_current_mirror()}/LiveFeed/GetGameZip?id={self._id}"
        info = session.get(url).text
        self._json_info = loads(info).get('Value')


    def is_fw_coef(self):
        coefs = self._json_info.get('E')
        if coefs:
            for c in coefs:
                if c.get('T') == 4055:
                    self._fw_coef = c.get('C')
                    return True

        return False

    def coefs_on_wins_in_rounds(self):
        coefs = self._json_info.get('E')
        if coefs:
            for c in coefs:
                if c.get('T') == 2140:
                    self._first_win_coef = c.get('C')
                if c.get('T') == 2141:
                    self._second_win_coef = c.get('C')

    def init_fighters(self):
        self._left_fighter = self._json_info.get('O1')
        self._right_fighter = self._json_info.get('O2')

    def is_fw(self):
        return bool(self._fw_coef)

    @property
    def fighters(self):
        return f"{self._left_fighter} - {self._right_fighter}"


    @property
    def id(self):
        return self._id
