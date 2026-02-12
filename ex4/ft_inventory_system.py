#!/usr/bin/env python3

def main() -> None:
    """Run the main program."""
    print("=== Inventory System Analysis ===")
    inventory = {"sword": 1,
                 "potion": 5,
                 "shield": 2,
                 "armor": 3,
                 "helmet": 1}
    item_count = 0
    for item in inventory.values():
        item_count += item
    print(f"Total items in inventory: {item_count}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===\n")
    for item in inventory:
        print(f"{item}: {inventory[item]} "
              f"{"unit" if inventory[item] == 1 else "units"} "
              f"({(inventory[item] / item_count * 100):.2f} %)")
    print("\n=== Inventory Statistics ===\n")
    most_abundant = {"": 0}
    for item in inventory:
        if inventory[item] > most_abundant[0]:
            pass


if __name__ == "__main__":
    main()
