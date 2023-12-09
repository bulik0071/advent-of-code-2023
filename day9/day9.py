print("Hello 9th day AOC2023!")


def parse_input(puzzles:str):
    output=[]
    for single_line in puzzles.split('\n'):
        aux_list=single_line.split(' ')
        for index_, element in enumerate(aux_list):
            aux_list[index_]=int(element)
        output.append(aux_list)
    return output
#test
#puzzle_9
def part_1():
    with open("day9/puzzle_9.txt","r") as f:
        answer=0
        lists_to_process=parse_input(f.read())
        for list_to_process in lists_to_process:
            big_list=[]
            big_list.append(list_to_process)
            while True:
                second_aux_list=[]
                for index_el,element in enumerate(big_list[-1]):
                    try:
                        second_aux_list.append(big_list[-1][index_el+1]-element)
                    except Exception as e:
                        continue
                big_list.append(second_aux_list)
                all_zeros=True
                for elemental in big_list[-1]:
                    if elemental != 0:
                        all_zeros=False
                        break
                if all_zeros:
                    big_list.reverse()
                    for i,small_list in enumerate(big_list):
                        try:
                            big_list[i+1].append(small_list[-1]+big_list[i+1][-1])
                        except Exception as e:
                            pass
                    history_value=big_list[-1][-1]
                    break
            answer=answer+history_value
        print(f"Answer p1: {answer}")
               
            
def part_2():

    with open("day9/puzzle_9.txt","r") as f:
        answer=0
        lists_to_process=parse_input(f.read())
        for list_to_process in lists_to_process:
            big_list=[]
            list_to_process.reverse()
            big_list.append(list_to_process)
            while True:
                second_aux_list=[]
                for index_el,element in enumerate(big_list[-1]):
                    try:
                        second_aux_list.append(big_list[-1][index_el+1]-element)
                    except Exception as e:
                        continue
                big_list.append(second_aux_list)
                all_zeros=True
                for elemental in big_list[-1]:
                    if elemental != 0:
                        all_zeros=False
                        break
                if all_zeros:
                    big_list.reverse()
                    for i,small_list in enumerate(big_list):
                        try:
                            big_list[i+1].append(small_list[-1]+big_list[i+1][-1])
                        except Exception as e:
                            pass
                    history_value=big_list[-1][-1]
                    break
            answer=answer+history_value
        print(f"Answer p1: {answer}")


if __name__=="__main__":
    part_1()
    part_2()

                