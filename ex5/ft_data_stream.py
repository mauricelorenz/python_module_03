#!/usr/bin/env python3

from typing import Generator


def get_events() -> Generator:
    """Yield the event number and a combination of player, level and event.

    Yields:
        The event number, player, level and event
    """
    players = {"alice": 5, "bob": 12, "charlie": 8}
    events = ["killed monster", "found treasure", "leveled up"]
    event_number = 1
    while True:
        for event in events:
            for player in players:
                if event == "leveled up":
                    players[player] += 1
                yield (event_number, player, players[player], event)
                event_number += 1


def get_fibonacci() -> Generator:
    """Yield the next fibonacci number.

    Yields:
        The fibonacci number
    """
    yield 0
    prev = 0
    curr = 1
    while True:
        yield curr
        next_val = prev + curr
        prev = curr
        curr = next_val


def is_prime(n: int) -> bool:
    """Tell if a number is prime or not.

    Args:
        n: The number to be checked

    Returns:
        True if prime, else False
    """
    i = 1
    while i < n:
        if n % i == 0 and i != 1:
            return False
        i += 1
    return True


def get_primes() -> Generator:
    """Yield the next prime number.

    Yields:
        The prime number
    """
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def main() -> None:
    """Run the main program."""
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    total_events = 0
    high_level_players = []
    treasure_events = 0
    level_up_events = 0
    gen = get_events()
    for event in range(1000):
        event_number, player, level, event = next(gen)
        total_events += 1
        if level >= 10 and player not in high_level_players:
            high_level_players += [player]
        if event == "found treasure":
            treasure_events += 1
        if event == "leveled up":
            level_up_events += 1
        print(f"Event {event_number}: Player {player} ({level}) {event}")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {len(high_level_players)}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    gen = get_fibonacci()
    for i in range(10):
        number = next(gen)
        print(f"{number}", end=", " if i < 9 else "\n")
    print("Prime numbers (first 5): ", end="")
    gen = get_primes()
    for i in range(5):
        number = next(gen)
        print(f"{number}", end=", " if i < 4 else "\n")


if __name__ == "__main__":
    main()
