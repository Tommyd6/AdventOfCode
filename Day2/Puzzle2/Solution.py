file_path = "Day2/Puzzle2/Puzzle_Input.txt"
my_dict = {
    "blue": 14,
    "red": 12,
    "green": 13 
}
import re
SumOfPowers=0
with open(file_path, 'r') as file:
    for line in file:
        Game,showed=line.split(":")
        Game_ID=Game.split(" ")[1]
        Valid=True
        showed=re.split(';|,',showed)
        my_dict = {
            "blue": 0,
            "red": 0,
            "green": 0 
        }
        for hand in showed:
            if(my_dict[hand.split()[1]]<int(hand.split()[0])):
                my_dict[hand.split()[1]]=int(hand.split()[0])
        SumOfPowers+=my_dict["blue"]*my_dict["red"]*my_dict["green"]
print(SumOfPowers)