print("Hello 11th day AOC2023!")
import re

def read_lines_from_file(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]

# Refactored Puzzle Solution
def relocate_galaxies(galaxies, axis, sky_map, expansion_value, original_galaxies):
    expansion_value = expansion_value - 1 if expansion_value != 1 else expansion_value
    additional_value = 0
    length_to_check = len(sky_map) if axis == 0 else len(sky_map[0])

    for i in range(1, length_to_check - 1):
        if all(galaxy[axis] != i for galaxy in original_galaxies):
            galaxies_to_relocate = [galaxy for galaxy in galaxies if galaxy[axis] > i + additional_value]
            
            for galaxy in galaxies_to_relocate:
                galaxies.remove(galaxy)
                y_expansion = expansion_value if axis == 0 else 0
                x_expansion = expansion_value if axis == 1 else 0
                galaxies.append((galaxy[0] + y_expansion, galaxy[1] + x_expansion))

            additional_value += expansion_value
    
    return galaxies

def calculate_total_distance(lines, expansion_value):
    original_galaxies = []
    sky_map = []

    for index, line in enumerate(lines):
        sky_map.append(list(line))
        for galaxy in re.finditer(r'#', line):
            original_galaxies.append((index, galaxy.start()))

    galaxies = original_galaxies.copy()
    galaxies = relocate_galaxies(galaxies, 0, sky_map, expansion_value, original_galaxies)
    galaxies = relocate_galaxies(galaxies, 1, sky_map, expansion_value, original_galaxies)

    total_distance = 0
    for i, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[i + 1:]:
            total_distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    return total_distance

lines = read_lines_from_file('day11/puzzle.txt')
print(calculate_total_distance(lines, 1))
print(calculate_total_distance(lines, 1000000))
