print("Hello first day Advent of Code 2023 part2!")
import re
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']

bad_looking_string='4nineeightseven2'

replacement_value_map = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

def find_two_digits(bad_looking_string:str):
    x = re.findall("[0-9]",bad_looking_string)
    if len(x) == 1:
        outnumber=int(str(x[0])+str(x[0]))
    else:
        outnumber=int(str(x[0])+str(x[-1]))
    return outnumber

def sanitize_bad_looking_line(bad_looking_string):
    new_string=''
    for ind,letter in enumerate(bad_looking_string):
        if letter.isdigit():
            new_string=new_string+letter
            continue
        for number in numbers:
            if bad_looking_string[ind:ind+len(number)].startswith(number):
                new_string=new_string+replacement_value_map[number]
                break
    return find_two_digits(bad_looking_string=new_string)


answer=0

with open("day1/puzzle_1.txt","r") as f:
    input_data = f.readlines()
    for single_line in input_data:
        single_line = single_line.strip()
        answer=answer+sanitize_bad_looking_line(bad_looking_string=single_line)


print(f"The correct answer for part 2 is: {answer}")
