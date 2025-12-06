from utils import read_input_file

DAY = "05"
TEST = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def split_range(s: str):
    a, b = s.split("-")
    return (int(a), int(b))


def part1(note: str):
    ranges, ingredient = note.split("\n\n")
    ranges = sorted(map(split_range, ranges.splitlines()))
    ingredient = sorted(map(int, ingredient.splitlines()))

    cnt = 0
    for i in ingredient:
        if any(a <= i <= b for a, b in ranges):
            cnt += 1

    return cnt


# TODO: implement solution for part 2
def part2(note: str):
    ranges, _ = note.split("\n\n")
    ranges = sorted(map(split_range, ranges.splitlines()))
    base = 0
    cnt = 0
    for a, b in ranges:
        if a > base:
            cnt += b - a + 1
        elif b > base:
            cnt += b - base
        else:
            continue
        base = b

    return cnt


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    assert part1(TEST) == 3
    print(part1(note))
    print("=== PART 2 ===")
    # TODO: replace test input's expected outcome
    assert part2(TEST) == 14
    print(part2(note))
