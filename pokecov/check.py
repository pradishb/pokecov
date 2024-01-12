from argparse import ArgumentParser

from pokecov import logger
from pokecov.coverage import get_coverage
from pokecov.coverage import get_data


def main():
    parser = ArgumentParser()
    parser.add_argument("types", nargs="+")
    parser.add_argument("--gen", default=6, type=int)
    args = parser.parse_args()

    data = get_data(args.gen)
    coverage = get_coverage(data, args.types)

    super = [t for t, e in coverage.items() if e == 2]
    normal = [t for t, e in coverage.items() if e == 1]
    not_very = [t for t, e in coverage.items() if e == 0.5]
    none = [t for t, e in coverage.items() if e == 0]

    super_str = ", ".join(super) if super != [] else "none"
    normal_str = ", ".join(normal) if normal != [] else "none"
    not_very_str = ", ".join(not_very) if not_very != [] else "none"
    none_str = ", ".join(none) if none != [] else "none"

    logger.info(
        f"Your attacks are super effective to {super_str} ({len(super)})."
    )
    logger.warning(
        "Your attacks have normal effectiveness to"
        f" {normal_str} ({len(normal)})."
    )
    logger.error(
        "Your attacks are not very effective to"
        f" {not_very_str} ({len(not_very)})."
    )
    logger.error(f"Your attacks have no effect to {none_str} ({len(none)}).")


if __name__ == "__main__":
    main()
