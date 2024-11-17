import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, "r") as input_file:
        data = json.load(input_file)
        sum_values = sum([item["score"] * item["weight"] for item in data])
        return round(sum_values, 3)


print(task())
