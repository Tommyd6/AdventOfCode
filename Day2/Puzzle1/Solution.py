file_path = "Day2/Puzzle1/Puzzle_Input.txt"
my_dict = {
    "blue": 14,
    "red": 12,
    "green": 13 
}
import re
SumOfValidGameID=0
with open(file_path, 'r') as file:
    for line in file:
        Game,showed=line.split(":")
        Game_ID=Game.split(" ")[1]
        Valid=True
        showed=re.split(';|,',showed)
        for hand in showed:
            if(my_dict[hand.split()[1]]<int(hand.split()[0])):
                Valid=False
        if(Valid):
            SumOfValidGameID+=int(Game_ID)
    print(SumOfValidGameID)