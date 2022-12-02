rock, paper, scissor = "A", "B", "C"
my_rock, my_paper, my_scissor = "X", "Y", "Z"

rock_score = 1
paper_score = 2
scissor_score = 3

l, d, w = 0, 3, 6

def get_score() -> None:
    cur = 0
    with open('input.txt') as f:
        rounds = f.read().split("\n")
        turns = [round.split(" ") for round in rounds]
        for turn in turns:
            enemy, my_turn = turn[0], turn[1]
            # enemy rock
            if enemy == rock:
                if my_turn == my_rock:
                    cur += rock_score + d
                elif my_turn == my_paper:
                    cur += paper_score + w
                elif my_turn == my_scissor:
                    cur += scissor_score + l
            # enemy paper
            elif enemy == paper:
                if my_turn == my_rock:
                    cur += rock_score + l
                elif my_turn == my_paper:
                    cur += paper_score + d
                elif my_turn == my_scissor:
                    cur += scissor_score + w
            # enemy scissor
            elif enemy == scissor:
                if my_turn == my_rock:
                    cur += rock_score + w
                elif my_turn == my_paper:
                    cur += paper_score + l
                elif my_turn == my_scissor:
                    cur += scissor_score + d
    return cur

score = get_score()
print(score)