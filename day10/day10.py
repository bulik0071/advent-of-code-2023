from queue import Queue
print("Hello 10th day AOC2023!")

def read_map(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def find_start_position(map_data):
    for y, line in enumerate(map_data):
        for x, char in enumerate(line):
            if char == "S":
                return x, y
    raise ValueError("Start position 'S' not found in map")

def initialize_queue(map_data, start_position, neighbor_directions):
    queue = Queue()
    x, y = start_position
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_char = map_data[y + dy][x + dx]
        if next_char in neighbor_directions:
            for dx2, dy2 in neighbor_directions[next_char]:
                if (x, y) == (x + dx + dx2, y + dy + dy2):
                    queue.put((1, (x + dx, y + dy)))
    return queue

def calculate_distances(map_data, neighbor_directions, start_position):
    dists = {start_position: 0}
    queue = initialize_queue(map_data, start_position, neighbor_directions)

    while not queue.empty():
        distance, (x, y) = queue.get()
        if (x, y) in dists:
            continue
        dists[(x, y)] = distance
        for dx, dy in neighbor_directions[map_data[y][x]]:
            queue.put((distance + 1, (x + dx, y + dy)))

    return dists

def count_inside_tiles(map_data, distances):
    width = len(map_data[0])
    height = len(map_data)
    inside_count = 0

    for y, line in enumerate(map_data):
        for x, char in enumerate(line):
            if (x, y) in distances:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < width and y2 < height:
                char2 = map_data[y2][x2]
                if (x2, y2) in distances and char2 not in ["L", "7"]:
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                inside_count += 1

    return inside_count

# Main code
map_data = read_map("day10/puzzle_10.txt")
start_position = find_start_position(map_data)

neighbor_directions = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

distances = calculate_distances(map_data, neighbor_directions, start_position)
print(f"Part 1: {max(distances.values())}")

inside_tiles_count = count_inside_tiles(map_data, distances)
print(f"Part 2: {inside_tiles_count}")
