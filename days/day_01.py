from aocd import get_data


def one() -> None:
    data = get_data(day=1, year=2024)

    left_side = []
    right_side = []

    for row in data.split("\n"):
        data_points = row.split("   ")

        left_side.append(int(data_points[0]))
        right_side.append(int(data_points[1]))

    left_side.sort()
    right_side.sort()

    row_abs = [abs(a - b) for a, b in zip(left_side, right_side)]
    print("Day 1:")
    print(f"    Part 1: {sum(row_abs)}")

    hash_map = {}

    row_similarity_score = []
    for row in left_side:
        if row not in hash_map:
            hash_map[row] = right_side.count(row)

        row_similarity_score.append(row * hash_map[row])

    print(f"    Part 2: {sum(row_similarity_score)}")
