def read_file() -> list:
    current_highest = 0
    with open('input.txt') as f:
        file_str = f.read().split("\n\n")
        for elf_obj in file_str:
            elf = elf_obj.split("\n")
            elf_ints = [int(i) for i in elf if i != ""]
            elf_sum = sum(elf_ints)
            if elf_sum > current_highest:
                current_highest = elf_sum
    return current_highest
        


highest = read_file()
print(highest)