from utils import read_input_file

DAY = "02"
TEST_NOTE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"


def to_range(s: str):
    lo, hi = s.strip().split("-")
    return (lo.strip(), hi.strip())


def part1(note: str):
    ranges = map(to_range, note.split(","))
    ans = 0
    for lo, hi in ranges:
        for length in range(2, len(hi) + 1, 2):
            k = length // 2
            start = 10 ** (k - 1)
            end = 10**k

            for half in range(start, end):
                full = int(str(half) * 2)
                if int(lo) <= full <= int(hi):
                    ans += full

    return ans


def part2(note: str):
    ranges = map(to_range, note.split(","))
    ans = set()
    for lo, hi in ranges:
        for n in range(len(lo), len(hi) + 1):
            for k in range(1, n // 2 + 1):
                if n % k:
                    continue
                m = n // k
                start = 10 ** (k - 1)
                end = 10**k
                for part in range(start, end):
                    num = int(str(part) * m)
                    if int(lo) <= num <= int(hi):
                        ans.add(num)

    return sum(ans)


if __name__ == "__main__":
    print(f"====== DAY {DAY} ======")
    note = read_input_file(DAY)
    print("=== PART 1 ===")
    assert part1(TEST_NOTE) == 1227775554
    print(part1(note))
    print("=== PART 2 ===")
    assert part2(TEST_NOTE) == 4174379265
    print(part2(note))
