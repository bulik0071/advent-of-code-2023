print("Hello 8th day AOC2023!")

def parse_input(puzzles:str):
    inst=puzzles.split('\n\n')
    instructions=[]
    for single_instruction in inst[0]:
        instructions.append(single_instruction)
    map_places_to_process=[]
    for map_place in inst[1].split('\n'):
        map_places_to_process.append(map_place)
    return instructions,map_places_to_process

def readInput08(infile):
    with open(infile) as f:
        l = f.read().split("\n\n")
        graph = {}
        for d in l[1].strip("\n").split('\n'):
            k = d.split(" = ")
            graph[k[0]] = k[1].replace("(","").replace(")","").split(", ")
        return l[0],graph

def create_lookup_dictionary(map_to_process:list):
    output_dictionary={}
    for single_destination in map_to_process:
        processed_destination=single_destination.replace('=','').replace('(','#').replace(',','#').replace(')','').replace(' ','#').split('#')
        _sing_dest=[]
        for element in processed_destination:
            if len(element)>0:
                _sing_dest.append(element)
        output_dictionary[_sing_dest[0]]={'L':_sing_dest[1],'R':_sing_dest[2]}
    return output_dictionary

def find_if_somethings_ends_with(string_to_find:str,string_to_lookup:str):
    if string_to_lookup.endswith(string_to_find):
        return True
    return False

def part_1():
    with open("day8/puzzle_8.txt","r") as f:
        instructions,map_places_to_process=parse_input(puzzles=f.read())
        map_dictionary=create_lookup_dictionary(map_to_process=map_places_to_process)
        actual_step='AAA'
        desired_destination='ZZZ'
        step_counter=0
        while True:
            for instruction in instructions:
                actual_step=map_dictionary[actual_step][instruction]
                step_counter=step_counter+1
                if actual_step==desired_destination:
                    return step_counter
import numpy as np

def path(instr,graph,start="AAA",end="ZZZ",mmax=0):
    mov = {"R":1, "L":0}
    pos = start
    i = 0
    m = 0
    while True:
        pos = graph[pos][mov[instr[i]]]
        m += 1
        if pos==end:
            return m                
        i+=1
        if i==len(instr):
            i=0
        if mmax and m>mmax:
            return None


def part_2():
    with open("day8/puzzle_8.txt","r") as f:
        instructions,map_places_to_process=readInput08("day8/puzzle_8.txt")
        starts = [ k for k in map_places_to_process.keys() if k[-1]=="A" ]
        ends = [ k for k in map_places_to_process.keys() if k[-1]=="Z" ]
        exits = []
        paths = []
        for s in starts:
            for e in ends:
                m = path(instr=instructions,graph=map_places_to_process,start=s,end=e,mmax=100000)
                if m:
                    exits.append(e)
                    paths.append(m)
                    continue
    return np.lcm.reduce(paths)
if __name__=="__main__":
    print(part_1())
    print(part_2())
