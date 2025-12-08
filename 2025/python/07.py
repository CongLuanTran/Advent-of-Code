from functools import cache

from utils import read_input_file

# TODO: replace the day
DAY = "07"
# TODO: provide test input
TEST = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


# TODO: implement solution for part 1
def part1(note: str):
    lines = note.strip().splitlines()
    beams = {lines[0].index("S")}
    ans = 0
    for ln in lines[1:]:
        splitters = set(filter(lambda i: ln[i] == "^", range(len(ln))))
        splits = splitters & beams
        if splits:
            ans += len(splits)
            beams ^= splits
            beams |= {ns for s in splits for ns in (s + 1, s - 1)}

    return ans


# TODO: implement solution for part 2
def part2(note: str):
    lines = note.strip().splitlines()
    end = len(lines)

    @cache
    def dfs(x, y):
        if y == end:
            return 1
        if lines[y][x] == "^":
            return dfs(x - 1, y + 1) + dfs(x + 1, y + 1)
        return dfs(x, y + 1)

    return dfs(lines[0].index("S"), 1)


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    # TODO: replace test input's expected outcome
    assert part1(TEST) == 21
    print(part1(note))
    print("=== PART 2 ===")
    # TODO: replace test input's expected outcome
    assert part2(TEST) == 40
    print(part2(note))
