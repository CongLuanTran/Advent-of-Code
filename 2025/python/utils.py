from pathlib import Path

INPUT_FOLDER = "./input"


def read_input_file(day: str):
    path = Path(INPUT_FOLDER) / f"{day}.txt"
    with open(path, "r") as f:
        return f.read()
