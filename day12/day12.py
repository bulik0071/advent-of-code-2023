from functools import cache
print("Hello 12th day AOC2023!")

@cache
def count_legal_arrangements(spring_pattern, group_counts):
    spring_pattern = spring_pattern.lstrip('.')

    if not spring_pattern:
        return int(not group_counts)

    if not group_counts:
        return int('#' not in spring_pattern)

    if spring_pattern[0] == '#':
        if len(spring_pattern) < group_counts[0] or '.' in spring_pattern[:group_counts[0]]:
            return 0  # Not enough space or operational spring within the group
        elif len(spring_pattern) == group_counts[0]:
            return int(len(group_counts) == 1)  # Single group of the right size
        elif spring_pattern[group_counts[0]] == '#':
            return 0  # Adjacent groups must be separated
        else:
            return count_legal_arrangements(spring_pattern[group_counts[0]+1:], group_counts[1:])

    return (count_legal_arrangements('#' + spring_pattern[1:], group_counts) + 
            count_legal_arrangements(spring_pattern[1:], group_counts))

with open("day12/puzzle.txt") as file:
    lines = [line.strip().split() for line in file.readlines()]
    spring_data = [(pattern, tuple(map(int, counts.split(',')))) for pattern, counts in lines]

total_arrangements_part1 = sum(count_legal_arrangements(pattern, counts) for pattern, counts in spring_data)
print("Part 1 total:", total_arrangements_part1)

spring_data_part2 = [(pattern * 5, counts * 5) for pattern, counts in spring_data]
total_arrangements_part2 = sum(count_legal_arrangements(pattern, counts) for pattern, counts in spring_data_part2)
print("Part 2 total:", total_arrangements_part2)
