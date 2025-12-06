from functools import reduce

from utils import read_input_file

DAY = "01"
TEST_NOTE = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def parse_turn(s: str):
    sign, value = s[0], s[1:]
    value = int(value)
    return value if sign == "R" else -value


def parse_input(note: str):
    return map(parse_turn, note.splitlines())


def at_zero(acc: tuple[int, int], move: int):
    pos, zero = acc
    return (pos := (pos + move) % 100, zero + (pos == 0))


def part1(note: str):
    return reduce(at_zero, parse_input(note), (50, 0))[1]


def cross_zero(acc: tuple[int, int], move: int):
    pos, zero = acc
    q = int(move / 100)
    r = move - q * 100
    return (
        (pos + r) % 100,
        zero + q + (r != 0 and pos != 0 and not (0 < pos + r < 100)),
    )


def part2(note: str):
    return reduce(cross_zero, parse_input(note), (50, 0))[1]


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    assert part1(TEST_NOTE) == 3
    print(part1(note))
    print("=== PART 2 ===")
    assert part2(TEST_NOTE) == 6
    print(part2(note))
