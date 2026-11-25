"""Split a restaurant bill between friends, tip included.

    python3 split.py 80 4 20    ->  Each pays $24.00
"""

import sys


def split(total, people, tip_percent=0):
    """What each person pays, rounded to the cent."""
    if people < 1:
        raise ValueError("Someone has to pay")
    with_tip = total * (1 + tip_percent)
    return round(with_tip / people, 2)


def main(args):
    total, people = float(args[0]), int(args[1])
    tip = float(args[2]) if len(args) > 2 else 0
    return f"Each pays ${split(total, people, tip):.2f}"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: python3 split.py TOTAL PEOPLE [TIP_PERCENT]")
    print(main(sys.argv[1:]))
