from aocd import get_data


def four():
    data = get_data(day=4, year=2024)

    text_map = []

    for row in data.split("\n"):
        text_map.append(list(row))

    DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def count_xmas_in_direction(char_index, row_index, dx, dy):
        try:
            if (
                not 0 < row_index + dy <= len(text_map)
                or not 0 < row_index + 2 * dy <= len(text_map)
                or not 0 < row_index + 3 * dy <= len(text_map)
            ):
                return 0

            if (
                not 0 < char_index + dx <= len(text_map[0])
                or not 0 < char_index + 2 * dx <= len(text_map[0])
                or not 0 < char_index + 3 * dx <= len(text_map[0])
            ):
                return 0

            possible_xmas_string = f"{text_map[row_index][char_index]}{text_map[row_index + dy][char_index + dx]}{text_map[row_index + 2*dy][char_index + 2*dx]}{text_map[row_index + 3*dy][char_index + 3*dx]}"
            if possible_xmas_string == "XMAS":
                return 1

            return 0
        except IndexError:
            return 0

    part_one = 0
    for row_index, row in enumerate(text_map):
        for char_index, char in enumerate(row):
            if char == "X":
                for dy, dx in DIRECTIONS:
                    part_one += count_xmas_in_direction(
                        char_index=char_index, row_index=row_index, dx=dx, dy=dy
                    )

    print("Day 4:")
    print(f"    Part 1: {part_one}")
