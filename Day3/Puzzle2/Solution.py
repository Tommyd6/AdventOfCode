import math as m, re

file_path = "Day3/Puzzle1/Puzzle_Input.txt"
board = list(open(file_path))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}
        print(edge)
        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(m.prod(p) for p in chars.values() if len(p)==2))