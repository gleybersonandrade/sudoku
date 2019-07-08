"""Sudoku main."""

# System imports
import argparse

# Local imports
from config import DESCRIPTION
from graph import Graph
from utils import execute, read_file


def main():
    """Responsible for main control."""
    parser = argparse.ArgumentParser(description=DESCRIPTION.get("MAIN"))
    parser.add_argument('-i', '--input', help=DESCRIPTION.get("INPUT"))
    args = parser.parse_args()
    try:
        if not args.input:
            raise ValueError
        values = read_file(args.input)
        graph = Graph(values)
        execute(graph)
    except ValueError:
        parser.print_help()


if __name__ == "__main__":
    main()
