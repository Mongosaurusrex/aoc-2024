from aocd import get_data


def is_safe(levels):
    is_ascending = None
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if 1 <= diff <= 3:
            if is_ascending is None:
                is_ascending = True
            elif not is_ascending:
                return False
        elif -3 <= diff <= -1:
            if is_ascending is None:
                is_ascending = False
            elif is_ascending:
                return False
        else:
            return False
    return True


def is_safe_with_skip(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if is_safe(new_levels):
            return True
    return False


def two():
    data = get_data(day=2, year=2024).split("\n")

    safe_reports_1 = sum(is_safe([int(x) for x in report.split()]) for report in data)

    safe_reports_2 = sum(
        is_safe([int(x) for x in report.split()])
        or is_safe_with_skip([int(x) for x in report.split()])
        for report in data
    )

    print("Day 2:")
    print(f"    Part 1: {safe_reports_1}")
    print(f"    Part 2: {safe_reports_2}")
