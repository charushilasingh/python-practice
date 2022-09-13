# Problem : Find the green Marble
# Descriptipn :
# Mariah recently started a marble collection that consistes of the following marbles and quantities
# red 2
# orange 1
# pink 3
# yellow 2

# secret bag consists of
# blue 3
# green 4
# orange 1
# purple 2
# yellow 2
# pink 2
# red 4
import random

# mariascollection
collection_maria = ["red", "pink", "orange", "red", "pink", "yellow", "pink", "yellow"]
# creation of secret bag
secret_bag = [
    "pink",
    "blue",
    "green",
    "orange",
    "red",
    "purple",
    "green",
    "blue",
    "blue",
    "red",
    "geen",
    "purple",
    "yellow",
    "red",
    "pink",
    "red",
    "green",
    "yellow",
]
# create list for marbles chosen
marbles_chosen = []
# track and tries remaining
# the marblestorehas a scrictrule for the secret bag : only five attempts : conter to track the trial
trie_remaining = 5
# create a for loop to iterate
for x in range(6):
    if trie_remaining > 0:
        selection = random.choice(secret_bag)
        marbles_chosen.append(selection)
        trie_remaining -= 1
        if selection == "green":
            collection_maria.append(selection)
            secret_bag.remove(selection)
            if "green" in collection_maria:
                print(
                    f"awesome! you found  green marble.If you would like  another marble, yoy have{trie_remaining} picks left."
                )
                break

    else:
        print(
            "sorry, you are out of trials. please come back tommorow and try your luck"
        )
print(f"Here are all the marbles that were chosen: {marbles_chosen}")
