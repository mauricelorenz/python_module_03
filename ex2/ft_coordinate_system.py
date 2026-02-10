#!/usr/bin/env python3

import sys
import math


def get_distance(pos1: tuple, pos2: tuple) -> float:
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 +
                     (pos2[2] - pos1[2]) ** 2)


def parse_coordinates(coord_str: str) -> tuple | None:
    try:
        coord_list = coord_str.split(",")
        coordinates = (int(coord_list[0]), int(coord_list[1]), int(coord_list[2]))
        print(f"Parsing coordinates: \"{coord_str}\"")
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coord_str}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
        return None
    print(f"Parsed position: {coordinates}")
    return coordinates


def run_example() -> None:
    spawn = (0, 0, 0)
    pos_a = (10, 20, 5)
    print(f"Position created: {pos_a}")
    print(f"Distance between {spawn} and {pos_a}: "
          f"{get_distance(spawn, pos_a):.2f}\n")
    pos_b = parse_coordinates("3,4,0")
    print(f"Distance between {spawn} and {pos_b}: "
          f"{get_distance(spawn, pos_b):.2f}\n")
    parse_coordinates("abc,def,ghi")
    print("\nUnpacking demonstration:")
    print("Player at x=3, y=4, z=0")
    print("Coordinates: X=3, Y=4, Z=0")


def main() -> None:
    """Run the main program."""
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) < 2:
        run_example()
    else:
        spawn = (0, 0, 0)
        for arg in sys.argv[1:]:
            pos = parse_coordinates(arg)
            print(f"Distance between {spawn} and {pos}: "
                  f"{get_distance(spawn, pos):.2f}\n")


if __name__ == "__main__":
    main()
