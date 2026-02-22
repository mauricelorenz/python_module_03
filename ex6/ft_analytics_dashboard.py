#!/usr/bin/env python3

def list_comp(players: dict) -> None:
    """Demonstrate List Comprehension.

    Args:
        players: The players used as example
    """
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): "
          f"{[player for player in players if players[player][0] > 2000]}")
    print(f"Scores doubled: {[2 * players[player][0] for player in players]}")
    print(f"Active players: "
          f"{[player for player in players if players[player][1]]}")


def dict_comp(players: dict, achievement_counts: dict) -> None:
    """Demonstrate Dict Comprehension.

    Args:
        players: The players used as example
        achievement_counts: The amount of achievements per player
    """
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {player: players[player][0] for player in
                     players if players[player][1]}
    print(f"Player scores: {player_scores}")
    score_categories = {"super high": 4,
                        "high": 3,
                        "medium": 2,
                        "low": 1,
                        "super low": 0}
    categories_filtered = {name: score_categories[name] for name in
                           score_categories if 4 > score_categories[name] > 0}
    print(f"Score categories: {categories_filtered}")
    print(f"Achievement counts: {achievement_counts}")


def set_comp(players: dict, achievements: dict,
             achievement_counts: dict) -> None:
    """Demonstrate Set Comprehension.

    Args:
        players: The players used as example
        achievements: The dict of each player's achievements
        achievement_counts: The amount of achievements per player
    """
    print("\n=== Set Comprehension Examples ===")
    unique_players = {player for player in achievements}
    print(f"Unique players: {unique_players}")
    unique_achievements = {achievement for player in achievements
                           for achievement in achievements[player]}
    print(f"Unique achievements: {unique_achievements}")
    regions = {"north": True,
               "east": True,
               "west": False,
               "south": False,
               "central": True}
    active_regions = {region for region in regions if regions[region]}
    print(f"Active regions: {active_regions}")
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    all_scores = [players[player][0] for player in players]
    avg_score = sum(all_scores) / len(all_scores)
    print(f"Average score: {avg_score}")
    top_performer = [player for player in players
                     if players[player][0] == max(all_scores)]
    print(f"Top performer: {top_performer[0]} ({players[top_performer[0]][0]} "
          f"points, {achievement_counts[top_performer[0]]} achievements)")


def main() -> None:
    """Run the main program."""
    print("=== Game Analytics Dashboard ===\n")
    players = {"alice": [2300, True],
               "bob": [1800, True],
               "charlie": [2150, True],
               "diana": [2050, False]}
    list_comp(players)
    achievements = {"alice": ["first_blood", "pixel_perfect", "speed_runner",
                              "first_blood", "first_blood"],
                    "bob": ["level_master", "boss_hunter", "treasure_seeker",
                            "level_master", "level_master"],
                    "charlie": ["treasure_seeker", "boss_hunter", "combo_king",
                                "first_blood", "boss_hunter", "first_blood",
                                "boss_hunter", "first_blood"],
                    "diana": ["first_blood", "combo_king", "level_master",
                              "treasure_seeker", "speed_runner", "combo_king",
                              "combo_king", "level_master"]}
    achievement_counts = {name: len(achievements[name])
                          for name in achievements}
    dict_comp(players, achievement_counts)
    set_comp(players, achievements, achievement_counts)


if __name__ == "__main__":
    main()
