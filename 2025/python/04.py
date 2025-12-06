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
    diagram = note.splitlines()
    w = len(diagram[0])
    h = len(diagram)
    cnt = 0

    for y in range(h):
        for x in range(w):
            if diagram[y][x] != "@":
                continue
            adj = 0
            for dy, dx in direction:
                if (
                    0 <= y + dy < h
                    and 0 <= x + dx < w
                    and diagram[y + dy][x + dx] == "@"
                ):
                    adj += 1
                    if adj >= 4:
                        break
            else:
                cnt += 1

    return cnt


def part2(note: str):
    diagram = [list(line) for line in note.splitlines()]
    w = len(diagram[0])
    h = len(diagram)
    cnt = 0

    while True:
        can_remove = 0
        for y in range(h):
            for x in range(w):
                if diagram[y][x] != "@":
                    continue
                adj = 0
                for dy, dx in direction:
                    if (
                        0 <= y + dy < h
                        and 0 <= x + dx < w
                        and diagram[y + dy][x + dx] == "@"
                    ):
                        adj += 1
                        if adj >= 4:
                            break
                else:
                    can_remove += 1
                    diagram[y][x] = "x"
        if not can_remove:
            break
        cnt += can_remove

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
