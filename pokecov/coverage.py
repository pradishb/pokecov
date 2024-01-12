import csv
from pathlib import Path
from typing import Dict
from typing import Iterable
from typing import List

BASE_PATH = Path(__file__).parent


def get_data(gen: int):
    if gen <= 1:
        file = BASE_PATH / "gen1.csv"
    elif 2 <= gen <= 5:
        file = BASE_PATH / "gen2.csv"
    else:
        file = BASE_PATH / "gen6.csv"

    with open(file) as fp:
        reader = csv.reader(fp)
        return list(reader)


def get_coverage(data: List[List[str]], types: Iterable[str]):
    types = [i.upper() for i in types]
    coverage: Dict[str, float] = {}
    for i in data:
        attack, defense, effectiveness = i
        if attack.upper() in types:
            old_value = coverage.get(defense, -1)
            new_value = float(effectiveness)
            if new_value > old_value:
                coverage[defense] = new_value
    return coverage
