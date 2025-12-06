from utils import read_input_file

# TODO: replace the day
DAY = "NN"
# TODO: provide test input
TEST = """<TEST-INPUT>"""


# TODO: implement solution for part 1
def part1(note: str):
    pass


# TODO: implement solution for part 2
def part2(note: str):
    pass


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    # TODO: replace test input's expected outcome
    assert part1(TEST) == 0
    print(part1(note))
    print("=== PART 2 ===")
    # TODO: replace test input's expected outcome
    assert part2(TEST) == 0
    print(part2(note))
