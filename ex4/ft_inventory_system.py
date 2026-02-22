#!/usr/bin/env python3


def inv_sys(inventory: dict) -> int:
    """Print total and unique items.

    Args:
        inventory: The dict containing items and their amount

    Returns:
        The total amount of items in the inventory
    """
    print("=== Inventory System Analysis ===")
    item_count = 0
    for item in inventory.values():
        item_count += item
    print(f"Total items in inventory: {item_count}")
    print(f"Unique item types: {len(inventory)}")
    return item_count


def curr_inv(inventory: dict, item_count: int) -> None:
    """Print all items with amount and percentage.

    Args:
        inventory: The dict containing items and their amount
        item_count: The total amount of items in the inventory
    """
    print("\n=== Current Inventory ===")
    for item in inventory:
        print(f"{item}: {inventory[item]} "
              f"{'unit' if inventory[item] == 1 else 'units'} "
              f"({(inventory[item] / item_count * 100):.1f}%)")


def inv_stat(inventory: dict) -> None:
    """Print the most and least abundant item.

    Args:
        inventory: The dict containing items and their amount
    """
    print("\n=== Inventory Statistics ===")
    most_abundant_value = 0
    for item in inventory:
        if inventory[item] > most_abundant_value:
            most_abundant_value = inventory[item]
            most_abundant_item, most_abundant_amount = item, inventory[item]
    print(f"Most abundant: {most_abundant_item} ({most_abundant_amount} "
          f"{'unit' if most_abundant_amount == 1 else 'units'})")
    least_abundant_value = most_abundant_value
    for item in inventory:
        if inventory[item] < least_abundant_value:
            least_abundant_value = inventory[item]
            least_abundant_item, least_abundant_amount = item, inventory[item]
    print(f"Least abundant: {least_abundant_item} ({least_abundant_amount} "
          f"{'unit' if least_abundant_amount == 1 else 'units'})")


def item_categ(inventory: dict) -> None:
    """Print the items categorized by their abundance.

    Args:
        inventory: The dict containing items and their amount
    """
    print("\n=== Item Categories ===")
    abundance_categ: dict = {"Moderate": {},
                             "Scarce": {}}
    for item in inventory:
        if inventory[item] > 3:
            abundance_categ["Moderate"][item] = inventory[item]
        else:
            abundance_categ["Scarce"][item] = inventory[item]
    print(f"Moderate: {abundance_categ['Moderate']}")
    print(f"Scarce: {abundance_categ['Scarce']}")


def management_sugg(inventory: dict) -> None:
    """Print the items that need to be restocked.

    Args:
        inventory: The dict containing items and their amount
    """
    print("\n=== Management Suggestions ===")
    print("Restock needed: "
          f"{[item for item in inventory if inventory[item] < 2]}")


def dict_prop_demo(inventory: dict) -> None:
    """Print a short demo of dictionary properties.

    Args:
        inventory: The dict containing items and their amount
    """
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {[item for item in inventory]}")
    print(f"Dictionary values: {[inventory[item] for item in inventory]}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    """Run the main program."""
    inventory: dict = {"sword": 1,
                       "potion": 5,
                       "shield": 2,
                       "armor": 3,
                       "helmet": 1}
    item_count = inv_sys(inventory)
    curr_inv(inventory, item_count)
    inv_stat(inventory)
    item_categ(inventory)
    management_sugg(inventory)
    dict_prop_demo(inventory)


if __name__ == "__main__":
    main()
