print("Hello 6th day AOC2023!")

def parse_input(puzzle:str):
    times=[]
    distances=[]
    races=[]
    for single_time in puzzle.splitlines()[0].split(':')[1].split(' '):
        if len(single_time)>0:
            times.append(int(single_time))
    for single_distance in puzzle.splitlines()[1].split(':')[1].split(' '):
        if len(single_distance)>0:
            distances.append(int(single_distance))
    for _,r in enumerate(times):
        races.append({"time":r,"distance":distances[_]})
    return races

def parse_input_2(puzzle:str):
    time=''
    distance=''

    for single_time in puzzle.splitlines()[0].split(':')[1].split(' '):
        if len(single_time)>0:
            time=time+single_time
    for single_distance in puzzle.splitlines()[1].split(':')[1].split(' '):
        if len(single_distance)>0:
            distance=distance+single_distance
    return int(time),int(distance)

def calculate_possibilities(time_to_check):
    hold_button_possibilities=[]
    for x in range(0,time_to_check+1):
        hold_button_possibilities.append(x)
    return hold_button_possibilities
    
def part_1():
    with open("day6/puzzle_6.txt","r") as f:
        input_data = f.read()
        dict_of_races=parse_input(puzzle=input_data)
        ways_to_beat=[]
        for race in dict_of_races:
            counter=0
            for hold_button_time in calculate_possibilities(race["time"]):
                speed=hold_button_time*1
                time_to_move=race["time"]-hold_button_time
                distance_moved=speed*time_to_move
                if distance_moved>race["distance"]:
                    counter=counter+1
            ways_to_beat.append(counter)
            counter=0
        answer=1
        for way in ways_to_beat:
            answer=answer*way
        print(f"Answer p1: {answer}")        
        

def find_lower_bound(time_to_check:int,distance_to_verify:int):
    lower_bound=0
    while True:
        speed=lower_bound*1
        time_to_move=time_to_check-lower_bound
        distance_moved=speed*time_to_move
        if distance_moved>distance_to_verify:
            return lower_bound
        else:
            lower_bound=lower_bound+1
def part_2():
    with open("day6/puzzle_6.txt","r") as f:
        input_data = f.read()
        time,distance=parse_input_2(puzzle=input_data)
        lower_bound=find_lower_bound(time_to_check=time,distance_to_verify=distance)
        upper_bound=time-lower_bound
        answer=upper_bound-lower_bound+1
        print(f"Answer p2: {answer}")        
if __name__=="__main__":
    part_1()
    part_2()
    