file_path = "Day1/Puzzle1/Puzzle_Input.txt"
import re
SumofCallibration=0
range=re.compile(f'[{0}-{9}]')
with open(file_path, 'r') as file:
    for line in file:
        digits = range.findall(line)
        SumofCallibration=SumofCallibration+int(digits[0]+digits[-1])
print(SumofCallibration)
