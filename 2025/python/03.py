from utils import read_input_file

DAY = "03"
TEST = """987654321111111
811111111111119
234234234234278
818181911112111"""


def part1(note: str):
    banks = note.strip().splitlines()
    total = 0
    for bats in banks:
        bats = bats.strip()
        bat1 = max(bats[:-1])
        bat2 = max(bats[bats.index(bat1) + 1 :])
        total += int(bat1 + bat2)

    return total


def part2(note: str):
    banks = note.strip().splitlines()
    total = 0
    for bats in banks:
        bats = bats.strip()
        start = 0
        joltagens = ""
        for i in range(11, 0, -1):
            best = max(bats[start:-i])
            joltagens += best
            start += bats[start:-i].index(best) + 1
        joltagens += max(bats[start:])
        total += int(joltagens)

    return total


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    assert part1(TEST) == 357
    print(part1(note))
    print("=== PART 2 ===")
    assert part2(TEST) == 3121910778619
    print(part2(note))
