from time import sleep
from collections import deque

from get_data import get_data
from send_to_ch import send_msg



sended_ids = deque(maxlen=15)
sended_fighters = deque(maxlen=15)

while True:
    for g in get_data():
        if g.id not in sended_ids and g.fighters not in sended_fighters and g.is_fw():
            print(f"Sending: {g}")
            send_msg(str(g))
            sended_ids.append(g.id)
            sended_fighters.append(g.fighters)
            sleep(30)
        else:
            if g.id not in sended_ids:
                print(g)
