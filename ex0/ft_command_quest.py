#!/usr/bin/env python3

import sys


def main() -> None:
    """Run the main program."""
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        i = 0
        for arg in sys.argv:
            if i == 0:
                print(f"Program name: {sys.argv[i]}")
                print(f"Arguments received: {len(sys.argv) - 1}")
            else:
                print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    main()
