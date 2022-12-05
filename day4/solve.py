def compare_range(range_1: str, range_2: str) -> bool:
    first_lower, first_upper = range_1.split("-")
    second_lower, second_upper = range_2.split("-")

    first_l, first_u = int(first_lower), int(first_upper)
    second_l, second_u = int(second_lower), int(second_upper)


    if (second_l <= first_l) and (first_u <= second_u):
        return True
    elif (first_l <= second_l) and (second_u <= first_u):
        return True
    else:
        return False

def compare_overlap(range_1: str, range_2: str) -> bool:
    first_lower, first_upper = range_1.split("-") # 3, 8
    second_lower, second_upper = range_2.split("-") # 13, 98

    first_l, first_u = int(first_lower), int(first_upper)
    second_l, second_u = int(second_lower), int(second_upper)

    if first_l < second_l and first_u < second_l:
        return False
    elif second_l < first_l and second_u < first_l:
        return False
    elif first_l == second_l or first_l == second_u:
        return True
    elif first_u == second_l or first_u == second_u:
        return True
    else:
        return True


def get_assignments() -> None:
    with open('input.txt') as f:
        all = f.read().split("\n")

        count = 0
        overlap_count = 0

        for line in all:
            range_1, range_2 = line.split(",")
            in_range = compare_range(range_1, range_2)

            overlap = compare_overlap(range_1, range_2)
            if overlap:
                overlap_count += 1

            if in_range:
                count += 1
            else:
                continue

        print(count)
        print(overlap_count)


get_assignments()