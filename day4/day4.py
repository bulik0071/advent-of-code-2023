print("Hello 4th day AOC2023!")


def parse_input(single_line:str):
    winning_numbers_raw=single_line.split('|')[0].split(':')[1].split(' ')
    winning_numbers=[]
    for winning_number in winning_numbers_raw:
        if len(winning_number)>0:
            winning_numbers.append(int(winning_number))
    user_numbers_raw=single_line.split('|')[1].split(' ')
    user_numbers=[]
    for user_number in user_numbers_raw:
        if len(user_number)>0:
            user_numbers.append(int(user_number))
    return user_numbers, winning_numbers
    
def count_points_by_set(user_numbers:list, winning_numbers:list):
    counter=0
    points=0
    for user_number in user_numbers:
        for winning_number in winning_numbers:
            if user_number==winning_number:
                counter=counter+1
                if counter==1:
                    points=1
                elif counter==2:
                    points=2
                else:
                    points=points*2
    return points

def count_new_scratchpads(user_numbers:list, winning_numbers:list):
    counter=0
    for user_number in user_numbers:
        for winning_number in winning_numbers:
            if user_number==winning_number:
                counter=counter+1
    return counter



def test_1():
    with open("day4/test_puzzle.txt","r") as f:
        input_data = f.readlines()
        answer=0
        for single_line in input_data:
            single_line = single_line.strip()
            user_nos,winning_nos=parse_input(single_line=single_line)
            answer=answer+count_points_by_set(user_numbers=user_nos,winning_numbers=winning_nos)
    print(answer)
            
def part_1():
    with open("day4/puzzle_4.txt","r") as f:
        input_data = f.readlines()
        answer=0
        for single_line in input_data:
            single_line = single_line.strip()
            user_nos,winning_nos=parse_input(single_line=single_line)
            answer=answer+count_points_by_set(user_numbers=user_nos,winning_numbers=winning_nos)
    print(f"Answer p1: {answer}")

def test_2():
    with open("day4/test_puzzle.txt","r") as f:
        input_data = f.readlines()
        answer=0
        scratchpads=[]
        for single_line in input_data:
            single_line = single_line.strip()
            user_nos,winning_nos=parse_input(single_line=single_line)
            scratchpads.append({'no_of_cards':1,'winning_nos':count_new_scratchpads(user_numbers=user_nos,winning_numbers=winning_nos)})
        for index_,scratchpad in enumerate(scratchpads):
            if scratchpad['winning_nos']==0:
                continue
            else:
                for x in range(0,scratchpad['winning_nos']):
                    scratchpads[index_+1+x]['no_of_cards']+=scratchpad["no_of_cards"]
        for scratchpad in scratchpads:
            answer=answer+scratchpad['no_of_cards']
        print(answer)

def part_2():
    with open("day4/puzzle_4.txt","r") as f:
        input_data = f.readlines()
        answer=0
        scratchpads=[]
        for single_line in input_data:
            single_line = single_line.strip()
            user_nos,winning_nos=parse_input(single_line=single_line)
            scratchpads.append({'no_of_cards':1,'winning_nos':count_new_scratchpads(user_numbers=user_nos,winning_numbers=winning_nos)})
        for index_,scratchpad in enumerate(scratchpads):
            if scratchpad['winning_nos']==0:
                continue
            else:
                for x in range(0,scratchpad['winning_nos']):
                    scratchpads[index_+1+x]['no_of_cards']+=scratchpad["no_of_cards"]
        for scratchpad in scratchpads:
            answer=answer+scratchpad['no_of_cards']
    print(f"Answer p2: {answer}")

        


if __name__=="__main__":
    part_1()
    part_2()