rock, paper, scissor = "A", "B", "C"
l, d, w = "X", "Y", "Z"

rock_score = 1
paper_score = 2
scissor_score = 3

l_score, d_score, w_score = 0, 3, 6

def get_score() -> None:
    cur = 0
    with open('input.txt') as f:
        rounds = f.read().split("\n")
        data = [round.split(" ") for round in rounds]
        for rows in data:
            enemy, outcome = rows[0], rows[1]
            # enemy rock
            if enemy == rock:
                if outcome == l:
                    # my_turn = scissor
                    cur += l_score + scissor_score
                elif outcome == d:
                    # my_turn = rock
                    cur += d_score + rock_score
                elif outcome == w:
                    # my_turn = paper
                    cur += w_score + paper_score
            # enemy paper
            elif enemy == paper:
                if outcome == l:
                    # my_turn = rock
                    cur += l_score + rock_score
                elif outcome == d:
                    # my_turn = paper
                    cur += d_score + paper_score
                elif outcome == w:
                    # my_turn = scissor
                    cur += w_score + scissor_score
            # enemy scissor
            elif enemy == scissor:
                if outcome == l:
                    # my_turn = paper
                    cur += l_score + paper_score
                elif outcome == d:
                    # my_turn = scissor
                    cur += d_score + scissor_score
                elif outcome == w:
                    # my_turn = rock
                    cur += w_score + rock_score
    return cur

score = get_score()
print(score)