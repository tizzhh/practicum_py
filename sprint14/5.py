from itertools import permutations


def tsp(places, distances):
    movements = len(places) - 1
    min_path = None
    min_path_len = float('inf')
    for path in permutations(places):
        cur_path_length = 0
        for movement in range(movements):
            cur_point, next_point = path[movement], path[movement + 1]
            point1_indx, point2_indx = places.index(cur_point), places.index(
                next_point
            )
            cur_path_length += distances[point1_indx][point2_indx]
        if cur_path_length < min_path_len:
            min_path_len = cur_path_length
            min_path = path
    return min_path_len, min_path


if __name__ == '__main__':
    places_example = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')
    distances_example = (
        (0, 3570, 2230, 6430, 600),
        (3570, 0, 5280, 4530, 3315),
        (2230, 5280, 0, 6715, 2540),
        (6430, 4530, 6715, 0, 6400),
        (600, 3315, 2540, 6400, 0),
    )
    min_path_length_example, min_path_example = tsp(
        places_example, distances_example
    )
    print(min_path_length_example, min_path_example)
