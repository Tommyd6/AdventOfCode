file_path = "Day1/Puzzle1/Puzzle_Input.txt"
import re
SumofCallibration=0
range=re.compile(f'[{0}-{9}]')
numstrings=["one","two", "three", "four", "five", "six", "seven", "eight", "nine"
            ,"0","1","2","3","4","5","6","7","8","9"]
with open(file_path, 'r') as file:
    for line in file:
        LI=-1
        FI=100000
        FN=0
        SN=0
        FItemp=FI
        LItemp=LI
        Value=0
        for num in numstrings:
            Value=(Value+1)%10
            try:
                FItemp=line.index(num)
                LItemp=line.rindex(num)
            except:
                pass
            if(FItemp<FI):
                FI=FItemp
                FN=Value
            if(LItemp>LI):
                LI=LItemp
                LN=Value
        SumofCallibration=SumofCallibration+FN*10+LN
print(SumofCallibration)
