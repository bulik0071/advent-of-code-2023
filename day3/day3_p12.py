print("Hello 3rd day AOC2023!")

def get_surrounding_elements(lines, line_index, start, end):
    """
    Get surrounding elements of a number in the grid.
    """
    current_line = lines[line_index]
    surrounding_elements = []

    # Check the left side of the number
    if start != 0:
        surrounding_elements.append((current_line[start - 1], line_index, start - 1))

    # Check the right side of the number
    if end != len(current_line) - 1:
        surrounding_elements.append((current_line[end + 1], line_index, end + 1))

    # Check the line above the number
    if line_index != 0:
        for i in range(max(0, start - 1), min(len(current_line), end + 2)):
            surrounding_elements.append((lines[line_index - 1][i], line_index - 1, i))

    # Check the line below the number
    if line_index != len(lines) - 1:
        for i in range(max(0, start - 1), min(len(current_line), end + 2)):
            surrounding_elements.append((lines[line_index + 1][i], line_index + 1, i))

    return surrounding_elements

def is_valid_part_number(surrounding_elements):
    """
    Check if the number is a valid part number based on surrounding elements.
    """
    for element, _, _ in surrounding_elements:
        if not element.isdigit() and element != '.':
            return True
    return False

def calculate_parts_and_gear_ratios(lines):
    """
    Calculate the sum of part numbers and gear ratios.
    """
    part_sum = 0
    gear_ratios = {}
    gear_ratio_sum = 0

    for line_index, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                start = i
                while i < len(line) and line[i].isdigit():
                    i += 1
                end = i - 1
                number = int(line[start:i])
                surrounding_elements = get_surrounding_elements(lines, line_index, start, end)

                if is_valid_part_number(surrounding_elements):
                    part_sum += number
                    for symbol, x, y in surrounding_elements:
                        if symbol == '*' and (x, y) in gear_ratios:
                            gear_ratio_sum += gear_ratios[(x, y)] * number
                        gear_ratios[(x, y)] = number
            else:
                i += 1

    return part_sum, gear_ratio_sum

with open("day3/puzzle_3.txt") as file:
    lines = file.read().strip().split("\n")

part_sum, gear_ratio_sum = calculate_parts_and_gear_ratios(lines)

print(f"Answer for day3 part1: {part_sum}")
print(f"Answer for day3 part2: {gear_ratio_sum}")
