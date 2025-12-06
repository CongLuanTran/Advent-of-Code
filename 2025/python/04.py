from utils import read_input_file

DAY = "04"
TEST = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

direction = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
    (-1, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
]


def part1(note: str):
    grid = note.splitlines()
    rolls = {
        complex(x, y)
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c == "@"
    }
    neighbours = {
        r: {r + complex(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y}
        for r in rolls
    }

    return sum(1 for r in rolls if len(neighbours[r] & rolls) < 4)


def part2(note: str):
    grid = note.splitlines()
    rolls = {
        complex(x, y)
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c == "@"
    }
    neighbours = {
        r: {r + complex(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y}
        for r in rolls
    }
    cnt = 0
    while removals := {r for r in rolls if len(neighbours[r] & rolls) < 4}:
        rolls -= removals
        cnt += len(removals)

    return cnt


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    assert part1(TEST) == 13
    print(part1(note))
    print("=== PART 2 ===")
    assert part2(TEST) == 43
    print(part2(note))
