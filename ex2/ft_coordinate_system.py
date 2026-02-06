#!/usr/bin/env python3

import sys
import math


def get_distance(pos1: tuple, pos2: tuple) -> float:
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 +
                     (pos2[2] - pos1[2]) ** 2)


def parse_coordinates() -> tuple | None:
    try:
        coord_str = sys.argv[1].split(",")
        coordinates = (int(coord_str[0]), int(coord_str[1]), int(coord_str[2]))
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
        return None
    print(f"Parsed position: {coordinates}")
    return coordinates


def main() -> None:
    """Run the main program."""
    print("=== Game Coordinate System ===\n")
    spawn = (0, 0, 0)
    example_position = (10, 20, 5)
    print(f"Position created: {example_position}")
    print(f"Distance between {spawn} and {example_position}: "
          f"{get_distance(spawn, example_position):.2f}")
    parse_coordinates()


if __name__ == "__main__":
    main()
