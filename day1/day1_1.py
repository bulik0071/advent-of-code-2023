print("Hello first day AOC2023!")
import re
def find_two_digits(bad_looking_string:str):
    x = re.findall("[0-9]",bad_looking_string)
    if len(x) == 1:
        outnumber=int(str(x[0])+str(x[0]))
    else:
        outnumber=int(str(x[0])+str(x[-1]))
    return outnumber

answer=0

with open("day1/puzzle_1.txt","r") as f:
    input_data = f.readlines()
    for single_line in input_data:
        single_line = single_line.strip()
        answer=answer+find_two_digits(single_line)


print(f"The answer for part 1 is: {answer}")










