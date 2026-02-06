#!/usr/bin/env python3

import sys


def main() -> None:
    """Run the main program."""
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores += [int(arg)]
        except ValueError:
            pass
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    main()
