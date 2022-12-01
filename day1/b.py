def read_file() -> list:
    first = 0
    second = 0
    third = 0
    with open('input.txt') as f:
        file_str = f.read().split("\n\n")
        for line in file_str:
            elf = line.split("\n")
            elf_ints = [int(i) for i in elf if i != ""]
            elf_sum = sum(elf_ints)
            
            if elf_sum > first:
                third = second
                second = first
                first = elf_sum
            elif first > elf_sum > second:
                third = second
                second = elf_sum
            elif second > elf_sum > third:
                third = elf_sum
            else:
                continue
    
    return sum([first, second, third])
        


highest = read_file()
print(highest)