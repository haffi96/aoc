from collections import deque

positions = [7, 6, 5, 4, 3, 2, 1, 0]

def get_from_stack() -> None:
    with open('input.txt') as f:
        lines = f.read().split("\n")
        
        stack_rows = []
        for line in lines[:8]:
            new = []
            fmted = [line[i:i+4] for i in range(0, len(line), 4)]
            for f in fmted:
                new.append(f.strip(" "))

            stack_rows.append(new)
        
        no_of_stacks = len(stack_rows[0])
        queues = [deque() for i in range(no_of_stacks)]

        for row in stack_rows:
            for stack_n, crate in enumerate(row):
                if crate != "":
                    queues[stack_n].appendleft(crate)
                else:
                    continue

        # print(queues)
        moving_proc = lines[10:]
        moves = []
        for proc in moving_proc:
            splt = proc.split(" ")
            moves.append([splt[1], splt[3], splt[5]])

        for move in moves:
            quant = int(move[0])
            origin = int(move[1])
            dest = int(move[2])

            
            tmp = deque()
            for i in range(quant):
                tmp.append(queues[origin - 1].pop())

            for i in range(len(tmp)):
                queues[dest - 1].append(tmp.pop())

        # print(queues)s
        top = []
        for q in queues:
            top.append(q[-1])

        print(top)



get_from_stack()