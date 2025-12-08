from math import prod

from utils import read_input_file

DAY = "06"
TEST = r"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def part1(note: str):
    cols = [n.split() for n in note.splitlines()]
    rows = zip(*cols)
    ans = 0
    for r in rows:
        if r[-1] == "*":
            ans += prod(map(int, r[:-1]))
        else:
            ans += sum(map(int, r[:-1]))

    return ans


def part2(note: str):
    cols = [list(n) for n in note.splitlines()]
    rows = list(zip(*cols))
    val: list[int] = []
    ans = 0
    for row in rows[::-1]:
        n = "".join(row[:-1]).strip()
        if n:
            val.append(int(n))
            if row[-1] == "+":
                ans += sum(val)
            elif row[-1] == "*":
                ans += prod(val)
            else:
                continue
            val = []

    return ans


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    assert part1(TEST) == 4277556
    print(part1(note))
    print("=== PART 2 ===")
    assert part2(TEST) == 3263827
    print(part2(note))
