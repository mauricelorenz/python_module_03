#!/usr/bin/env python3

import sys
import math


def get_distance(pos_start: tuple, pos_end: tuple) -> float:
    """Calculate the distance between two positions.

    Args:
        pos_start: The starting point to calculate from
        pos_end: The end point to calculate to

    Returns:
        The euclidean distance between the two points
    """
    return math.sqrt((pos_end[0] - pos_start[0]) ** 2 +
                     (pos_end[1] - pos_start[1]) ** 2 +
                     (pos_end[2] - pos_start[2]) ** 2)


def parse_coordinates(coord_str: str) -> tuple | None:
    """Parse the passed string into a tuple.

    Args:
        coord_str: String containing comma separated values

    Returns:
        A tuple containing x, y and z variables
        None if the values are non-numeric or fewer than 3
    """
    try:
        coord_list = coord_str.split(",")
        coordinates = (int(coord_list[0]), int(coord_list[1]),
                       int(coord_list[2]))
        print(f"Parsing coordinates: \"{coord_str}\"")
    except (ValueError, IndexError) as e:
        print(f"Parsing invalid coordinates: \"{coord_str}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
        return None
    print(f"Parsed position: {coordinates}")
    return coordinates


def run_example() -> None:
    """Print an example output."""
    spawn = (0, 0, 0)
    pos_a = (10, 20, 5)
    print(f"Position created: {pos_a}")
    print(f"Distance between {spawn} and {pos_a}: "
          f"{get_distance(spawn, pos_a):.2f}\n")
    pos_b = parse_coordinates("3,4,0")
    if pos_b:
        print(f"Distance between {spawn} and {pos_b}: "
              f"{get_distance(spawn, pos_b):.2f}\n")
    parse_coordinates("abc,def,ghi")
    print("\nUnpacking demonstration:")
    if pos_b:
        (x, y, z) = pos_b
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    """Run the main program."""
    print("=== Game Coordinate System ===\n")
    argc = 0
    for arg in sys.argv:
        argc += 1
    if argc < 2:
        run_example()
    else:
        spawn = (0, 0, 0)
        i = 1
        for arg in sys.argv[1:]:
            pos = parse_coordinates(arg)
            if pos:
                print(f"Distance between {spawn} and {pos}: "
                      f"{get_distance(spawn, pos):.2f}")
            if i < argc - 1:
                print()
            i += 1


if __name__ == "__main__":
    main()
