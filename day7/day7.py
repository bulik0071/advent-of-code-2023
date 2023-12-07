print("Hello 7th day AOC2023!")

CARD_DISTINCT=['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_DISTINCT_2=['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
CARD_DISTINCT.reverse()
CARD_DISTINCT_2.reverse()
def determine_rank_of_hand(single_set:str):
    hand_set={}
    for card in single_set:
        if card in hand_set:
            hand_set[card]=hand_set[card]+1
        else:
            hand_set[card]=1
    values_counter=[]
    rank=1
    for v in hand_set.values():
        values_counter.append(v)
    if 5 in values_counter:
        rank=7
    if 4 in values_counter:
        rank=6
    if 3 in values_counter:
        if 2 in values_counter:
            rank=5
        else:
            rank=4
    if len(values_counter)==5:
        rank=1
    if len(values_counter)==3 and 2 in values_counter:
        rank=3
    if len(values_counter)==4:
        rank=2
    return {"single_set":single_set,"rank":rank,"bid":0}



def determine_rank_of_hand_p2(single_set:str):
    hand_set={}
    joker_counter=0
    for index,card in enumerate(single_set):
        if card=='J':
            joker_counter=joker_counter+1
        else:
            if card in hand_set:
                hand_set[card]=hand_set[card]+1
            else:
                hand_set[card]=1
    if joker_counter==5:
        hand_set['J']=5
    else:
        max_value=-1
        actual_key=''
        for key,value in hand_set.items():
            if value>max_value:
                max_value=value
                actual_key=key
            if value==max_value:
                if CARD_DISTINCT.index(key)<CARD_DISTINCT.index(actual_key):
                    actual_key=key
        hand_set[actual_key]=hand_set[actual_key]+joker_counter
            
    rank=1
    values_counter=[]
    for v in hand_set.values():
        values_counter.append(v)
    if 5 in values_counter:
        rank=7
    if 4 in values_counter:
        rank=6
    if 3 in values_counter:
        if 2 in values_counter:
            rank=5
        else:
            rank=4
    if len(values_counter)==5:
        rank=1
    if len(values_counter)==3 and 2 in values_counter:
        rank=3
    if len(values_counter)==4:
        rank=2
    return {"single_set":single_set,"rank":rank,"bid":0}
"""
Hurray let's finally do some sorting!
"""
example_set1="KK677"
example_set2="KTJJT"

def determine_which_set_is_stronger_on_the_same_rank(first_set:str,second_set:str):
    for letter_index,letter in enumerate(first_set):
        if CARD_DISTINCT.index(letter)<CARD_DISTINCT.index(second_set[letter_index]):
            return False
        elif CARD_DISTINCT.index(letter)==CARD_DISTINCT.index(second_set[letter_index]):
            continue
        else:
            return True

def bubbleSortRank(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]['rank'] > arr[j + 1]['rank']:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
            if arr[j]['rank']==arr[j+1]['rank']:
                if determine_which_set_is_stronger_on_the_same_rank(arr[j]['single_set'],arr[j+1]['single_set']):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True   
        if not swapped:
            return
        
        
def determine_which_set_is_stronger_on_the_same_rank_p2(first_set:str,second_set:str):
    for letter_index,letter in enumerate(first_set):
        if CARD_DISTINCT_2.index(letter)<CARD_DISTINCT_2.index(second_set[letter_index]):
            return False
        elif CARD_DISTINCT_2.index(letter)==CARD_DISTINCT_2.index(second_set[letter_index]):
            continue
        else:
            return True

def bubbleSortRank_p2(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]['rank'] > arr[j + 1]['rank']:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
            if arr[j]['rank']==arr[j+1]['rank']:
                if determine_which_set_is_stronger_on_the_same_rank_p2(arr[j]['single_set'],arr[j+1]['single_set']):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True   
        if not swapped:
            return
        
def part_12():
    with open("day7/puzzle_7.txt","r") as f:
        input_data = f.read().split('\n')
        list_to_process=[]
        list_to_process_2=[]
        for single_line in input_data:
            set_of_hands=determine_rank_of_hand(single_line.split(' ')[0])
            set_of_hands_p2=determine_rank_of_hand_p2(single_line.split(' ')[0])
            set_of_hands['bid']=int(single_line.split(' ')[1])
            set_of_hands_p2['bid']=int(single_line.split(' ')[1])
            list_to_process.append(set_of_hands)
            list_to_process_2.append(set_of_hands_p2)
        bubbleSortRank(list_to_process)
        bubbleSortRank_p2(list_to_process_2)
        rank_to_assign=1
        total_winnings=0
        for single_set in list_to_process:
            single_set['position']=rank_to_assign
            rank_to_assign+=1
            total_winnings=(single_set['position']*single_set['bid'])+total_winnings
        print(f"Answer p1: {total_winnings}")
        
        rank_to_assign=1
        total_winnings=0
        for single_set in list_to_process_2:
            single_set['position']=rank_to_assign
            rank_to_assign+=1
            total_winnings=(single_set['position']*single_set['bid'])+total_winnings
        print(f"Answer p2: {total_winnings}")        
             
if __name__=="__main__":
    part_12()
                