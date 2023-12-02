print("Hello 2nd day AOC2023!")

example='Game 4: 9 red, 3 green; 3 green, 8 red, 6 blue; 12 blue, 4 green, 6 red; 4 green, 18 blue, 11 red; 9 blue, 2 green, 3 red; 14 blue, 7 red'
example2='Game 19: 2 red, 9 green; 2 red, 1 blue; 5 blue, 12 green; 5 green; 8 green, 2 red, 3 blue; 1 red, 11 green'

set_example_1=' 3 green, 8 red, 6 blue'

MAX_RED=12
MAX_GREEN=13
MAX_BLUE=14

def get_game_id(some_string:str):
    game_id=some_string.split(":")[0].split(' ')[1]
    return game_id

def define_set(some_string:str):
    set_list=some_string.split(":")[1].split(';')
    return set_list

def define_elements(set_example:str):
    elements=set_example.replace(',','').split(' ')
    reversed_elements=elements[::-1]
    for element in reversed_elements:
        if element == '':
            reversed_elements.remove(element)
    return reversed_elements

def determine_possibility_of_the_game(puzzle_line:str):
    set_list=define_set(puzzle_line)
    is_game_possible=True
    
    for set_example in set_list:
        set_example_1=define_elements(set_example)
        is_game_possible=True
        for index_element,element in enumerate((set_example_1)):
            if is_game_possible==False:
                break
            if element == 'red':
                if int(set_example_1[index_element+1]) > MAX_RED:
                    is_game_possible=False
                    return is_game_possible

            elif element == 'green':
                if int(set_example_1[index_element+1]) > MAX_GREEN:
                    is_game_possible=False
                    return is_game_possible
            elif element == 'blue':
                if int(set_example_1[index_element+1]) > MAX_BLUE:
                    is_game_possible=False
                    return is_game_possible
            else:
                continue
    return is_game_possible



with open("day2/puzzle_2.txt","r") as f:
    input_data = f.readlines()
    answer=0
    for single_line in input_data:
        single_line = single_line.strip()
        if determine_possibility_of_the_game(single_line): 
           answer=answer+int(get_game_id(single_line))
           
print(f"Answer for day2 part1: {answer}")