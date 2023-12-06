print("Hello 5th day AOC2023!")

def remove_empty_elements(list_to_sanitize:list):
    list_to_return=[]
    for element in list_to_sanitize:
        if len(element)>0:
            try:
                list_to_return.append(int(element))
            except:
                mini_list=[]
                for mini_element in element.split(' '):
                    if len(mini_element)>0:
                        mini_list.append(int(mini_element))
                list_to_return.append(mini_list)
            
    return list_to_return

def parse_input(puzzles:str):
    raw_list=puzzles.split('\n\n')
    seeds_raw=raw_list[0].split(':')[1].split(' ')
    seeds=remove_empty_elements(seeds_raw)
    seed_to_soil_map_raw=raw_list[1].split(':')[1].split('\n')
    seed_to_soil_map=remove_empty_elements(seed_to_soil_map_raw)
    soil_to_fertilizer_map_raw=raw_list[2].split(':')[1].split('\n')
    soil_to_fertilizer_map=remove_empty_elements(soil_to_fertilizer_map_raw)
    fertilizer_to_water_map_raw=raw_list[3].split(':')[1].split('\n')
    fertilizer_to_water_map=remove_empty_elements(fertilizer_to_water_map_raw)
    water_to_light_map_raw=raw_list[4].split(':')[1].split('\n')
    water_to_light_map=remove_empty_elements(water_to_light_map_raw)
    light_to_temperature_map_raw=raw_list[5].split(':')[1].split('\n')
    light_to_temperature_map=remove_empty_elements(light_to_temperature_map_raw)
    temperature_to_humidity_map_raw=raw_list[6].split(':')[1].split('\n')
    temperature_to_humidity_map=remove_empty_elements(temperature_to_humidity_map_raw)
    humidity_to_location_map_raw=raw_list[7].split(':')[1].split('\n')
    humidity_to_location_map=remove_empty_elements(humidity_to_location_map_raw)
    humidity_to_location_map_raw=[]
    return seeds,seed_to_soil_map,soil_to_fertilizer_map,fertilizer_to_water_map,water_to_light_map,light_to_temperature_map,temperature_to_humidity_map,humidity_to_location_map
    
def map_using_strange_mapping_pattern(stupid_list:list,element_to_check):
    output=element_to_check
    for stupid_list_element in stupid_list:
        source=stupid_list_element[1]
        destination=stupid_list_element[0]
        length_range=stupid_list_element[2]
        source_plus_length=source+length_range
        if element_to_check>=source and element_to_check<=source_plus_length:
            difference=element_to_check-source
            output=difference+destination
            return output
    return output

def invert_map(stupid_list:list,element_to_check):
    output=element_to_check
    for stupid_list_element in stupid_list:
        destination=stupid_list_element[1]
        source=stupid_list_element[0]
        length_range=stupid_list_element[2]
        source_plus_length=source+length_range
        if element_to_check>=source and element_to_check<=source_plus_length:
            difference=element_to_check-source
            output=difference+destination
            return output
    return output
    
def prepare_sets_from_seeds(list_to_convert:list):
    set=[]
    for index_, list_ in enumerate(list_to_convert):
        if index_%2==0:
            set.append([list_,list_to_convert[index_+1]])
        else:
            continue
    return set
            
            
def part_1():
    with open("day5/puzzle_5.txt","r") as f:
        input_data = f.read()
        seeds,seed_to_soil_map,soil_to_fertilizer_map,fertilizer_to_water_map,water_to_light_map,light_to_temperature_map,temperature_to_humidity_map,humidity_to_location_map=parse_input(puzzles=input_data)
        answer=999999999999999999999999
        for seed in seeds:
            soil=map_using_strange_mapping_pattern(seed_to_soil_map,seed)
            fertilizer=map_using_strange_mapping_pattern(soil_to_fertilizer_map,soil)
            water=map_using_strange_mapping_pattern(fertilizer_to_water_map,fertilizer)
            light=map_using_strange_mapping_pattern(water_to_light_map,water)
            temperature=map_using_strange_mapping_pattern(light_to_temperature_map,light)
            humidity=map_using_strange_mapping_pattern(temperature_to_humidity_map,temperature)
            location=map_using_strange_mapping_pattern(humidity_to_location_map,humidity)
            if location<answer:
                answer=location
    print(f"Answer p1: {answer}")      
        
def part_2():
    with open("day5/puzzle_5.txt","r") as f:
        input_data = f.read()
        seeds,seed_to_soil_map,soil_to_fertilizer_map,fertilizer_to_water_map,water_to_light_map,light_to_temperature_map,temperature_to_humidity_map,humidity_to_location_map=parse_input(puzzles=input_data)
        answer=0
        location=0
        while True:
            seed_to_check=invert_map(seed_to_soil_map,invert_map(soil_to_fertilizer_map,invert_map(fertilizer_to_water_map,invert_map(water_to_light_map,invert_map(light_to_temperature_map,invert_map(temperature_to_humidity_map,invert_map(humidity_to_location_map,location)))))))
            print(location)
            for set in prepare_sets_from_seeds(seeds):
                if seed_to_check>=set[0] and seed_to_check<=set[0]+set[1]:
                    return location
            location=location+1
                
            

if __name__=="__main__":
    part_1()
    print(f"Answer p2: {part_2()}")
