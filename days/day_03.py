from aocd import get_data
import re


def three():
    def find_mul_matches(data: str):
        pattern = r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)"

        return re.findall(pattern, data)

    def pick_numbers_from_mul(mul: str) -> tuple[int]:
        pattern = r"\d{1,3}"

        result = re.findall(pattern, mul)

        return int(result[0]), int(result[1])

    def is_dont_command(command):
        return command == "don't()"

    def is_do_command(command):
        return command == "do()"

    data = get_data(day=3, year=2024)

    command_list = find_mul_matches(data=data)
    do_command = True
    part_one = 0
    part_two = 0
    for command in command_list:
        if is_dont_command(command):
            do_command = False
        elif is_do_command(command):
            do_command = True
        else:
            left, right = pick_numbers_from_mul(command)

            part_one += left * right
            if do_command:
                part_two += left * right

    print("Day 3:")
    print(f"    Part 1: {part_one}")
    print(f"    Part 2: {part_two}")
