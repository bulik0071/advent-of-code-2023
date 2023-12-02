print("Hello 2nd day AOC2023 part2!")


def parse_set(some_string:str):
    set_list=some_string.split(":")[1].replace(',','').replace(';','').split(' ')
    reversed_elements=set_list[::-1]
    for element in reversed_elements:
        if element == '':
            reversed_elements.remove(element)
    return reversed_elements

def find_minimum(color_name:str,list_to_verify:list):
    minimum_value=0
    for index_element,element in enumerate((list_to_verify)):
        if element == color_name:
            if int(list_to_verify[index_element+1]) > minimum_value:
                minimum_value=int(list_to_verify[index_element+1])
                
    return minimum_value
            

answer=0
with open("day2/puzzle_2.txt","r") as f:
    input_data = f.readlines()
    answer=0
    for single_line in input_data:
        green_cubes=0
        blue_cubes=0
        red_cubes=0
        single_line = single_line.strip()
        set_to_check=parse_set(single_line)
        green_cubes=find_minimum(color_name='green',list_to_verify=set_to_check)
        blue_cubes=find_minimum(color_name='blue',list_to_verify=set_to_check)
        red_cubes=find_minimum(color_name='red',list_to_verify=set_to_check)
        answer=answer+(green_cubes*blue_cubes*red_cubes)
        
print(f"Answer for day2 part2: {answer}")