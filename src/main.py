from time import sleep
from collections import deque

from get_data import get_data



sended = deque(maxlen=15)

while True:
    for g in get_data():
        if g.id not in sended and g.is_fw_coef():
            print(f"Sending: {g}")
            sended.append(g.id)
            sleep(30)
        else:
            if g.id not in sended:
                print(g)
