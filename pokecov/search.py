from argparse import ArgumentParser
from itertools import combinations
from typing import Set

from pokecov import logger
from pokecov.coverage import get_coverage
from pokecov.coverage import get_data


def main():
    parser = ArgumentParser()
    parser.add_argument("--min-count", default=6, type=int)
    parser.add_argument("--max-count", default=6, type=int)
    parser.add_argument("--gen", default=6, type=int)
    parser.add_argument("--ignore", nargs="*")
    parser.add_argument("--must-have", nargs="*")
    parser.add_argument("--cant-have", nargs="*")
    args = parser.parse_args()

    data = get_data(args.gen)
    all_types = set([i[0] for i in data])

    ignore_types: Set[str] = set(args.ignore) if args.ignore else set()
    must_have: Set[str] = set(args.must_have) if args.must_have else set()
    cant_have: Set[str] = set(args.cant_have) if args.cant_have else set()

    ignore_types = set(i.title() for i in ignore_types)
    must_have = set(i.title() for i in must_have)
    cant_have = set(i.title() for i in cant_have)

    for count in range(args.min_count, args.max_count + 1):
        for types in combinations(all_types - cant_have, count):
            if not set(types).issuperset(must_have):
                continue
            coverage = get_coverage(data, types)
            super = [
                t for t, e in coverage.items() if e == 2 or t in ignore_types
            ]
            if len(super) >= len(all_types):
                logger.info(", ".join(types))


if __name__ == "__main__":
    main()
