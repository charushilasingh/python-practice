# problem_kickball Teams
# players playing in todays game of kickball
# Anastasia
# eli
# jamal
# jada
# theo
# Michelle
# adam
# rhea
# charlie
# jasmine
# marley
# kenji
# sydney
# yara

import random

available_players = [
    "Anastasia",
    "eli",
    "jamal",
    "jada",
    "theo",
    "Michelle",
    "adam ",
    "rhea",
    "charlie",
    "jasmine ",
    "marley",
    "kenji",
    "sydney ",
    "yara",
]
# two captain teams
jaleesas_team = ["jaleesa"]
rahims_team = ["rahim"]
while len(jaleesas_team) < 8:
    player_selected = random.choice(available_players)
    jaleesas_team.append(player_selected)
    available_players.remove(player_selected)

    # remaining players adds to rahims team
rahims_team.extend(available_players)

# display
print("jaleesas_team")
print(*jaleesas_team, sep=" ,")
# print(available_players)
print("rahims_team")
print(*rahims_team, sep=" ,")
