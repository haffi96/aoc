def get_val(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    if letter.isupper():
        return ord(letter) - 64 + 26

def find_common_per_sack(sentence: str) -> str:
    str_len = len(sentence)
    s1 = slice(0, str_len // 2)
    s2 = slice(str_len // 2, str_len)
    first, second = sentence[s1], sentence[s2]
    common = ''.join(set(first).intersection(second))
    return common

def find_common_per_group(group: list[str]) -> str:
    assert len(group) == 3
    first = set(group[0])
    second = set(group[1])
    third = set(group[2])
    common = first & second & third
    val, *_ = common
    return val


def get_totals() -> None:
    with open('input.txt') as f:
        allsacks = f.read().split("\n")
        priorities = []
        for sack in allsacks:
            common = find_common_per_sack(sack)
            priorities.append(get_val(common))
        print(sum(priorities))

        groups = []
        for i in range(0, len(allsacks), 3):
            groups.append(allsacks[i:i+3])
        
        g_priorities = []
        for group in groups:
            common = find_common_per_group(group)
            g_priorities.append(get_val(common))
        
        print(sum(g_priorities))
            


get_totals()