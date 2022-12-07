from collections import deque

def get_market_pos(marker_len: int) -> None:
    with open('./input.txt') as f:
        cur = deque(maxlen=marker_len)
        data = f.read()
        for index, letter in enumerate(data):
            cur.append(letter)


            if len(cur) == marker_len:
                if len(cur) == len(set(cur)):
                    print(index + 1, cur)
                    break


get_market_pos(4)
get_market_pos(14)

